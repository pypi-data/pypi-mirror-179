from pdbmender.formats import new_pdb_line, read_pdb_line, read_pqr_line
from pdbmender.utils import mend_pdb
from pypka.clean.ffconverter import (
    AMBER_protomers,
    GROMOS_protomers,
    CHARMM_protomers,
    gromos2amber,
    gromos2charmm,
    mainchain_Hs,
)
import os
from formats import read_pdb_line


def fix_structure_states(
    outputname,
    pH,
    ff_out,
    sites,
    tit_atoms,
    other_atoms,
    cys_bridges,
    delphi_input_content,
    renumbered,
    terminal_offset,
):

    ff_protomer = {
        "amber": AMBER_protomers,
        "gromos_cph": GROMOS_protomers,
        "charmm": CHARMM_protomers,
    }[ff_out]
    pdb_content = (
        f"REMARK     PypKa assigned protonation states @ pH {pH}\n"
        "REMARK     Residue    Avg Prot   State Prob    Taut Prob\n"
    )
    new_states = {}
    resnumb_sites = {}
    termini = {}
    for chain, sites_list in sites.items():
        for site in sites_list:
            (
                resname,
                resnumb,
                termini_resname,
                most_prob_taut,
                state_prob,
                taut_prob,
                tit_curve,
            ) = site
            (pdb_content, new_state, new_resname, remove_hs) = getProtomerResname(
                pdb_content,
                pH,
                ff_protomer,
                resnumb,
                resname,
                most_prob_taut,
                state_prob,
                taut_prob,
                tit_curve,
            )
            if resname in ("NTR", "CTR"):
                new_resname = termini_resname
                if chain not in termini:
                    termini[chain] = {}
                termini[chain][resnumb] = termini_resname
            if chain not in new_states:
                new_states[chain] = {}
            new_states[chain][resnumb] = (resname, new_state, new_resname, remove_hs)
            if chain not in resnumb_sites:
                resnumb_sites[chain] = []
            resnumb_sites[chain].append(resnumb)

    new_pdb = pdb_content
    counter = 0

    in_delphi_pdb = {}
    for line in delphi_input_content:
        if line.startswith("ATOM "):
            (aname, anumb, resname, chain, resnumb, x, y, z) = read_pdb_line(line)
            if chain not in in_delphi_pdb:
                in_delphi_pdb[chain] = {}
            if resnumb not in in_delphi_pdb[chain]:
                in_delphi_pdb[chain][resnumb] = []
            in_delphi_pdb[chain][resnumb].append(aname)

    for line in delphi_input_content:
        if line.startswith("ATOM "):
            (aname, anumb, resname, chain, resnumb, x, y, z) = read_pdb_line(line)

            if anumb in tit_atoms:
                # molecule = tit_atoms[anumb]
                (oldresname, new_state, resname, removeHs) = new_states[chain][resnumb]
                if aname in removeHs:
                    continue
                if (
                    ff_out == "amber"
                    and oldresname in gromos2amber
                    and new_state in gromos2amber[oldresname]
                    and aname in gromos2amber[oldresname][new_state]
                ):
                    aname = gromos2amber[oldresname][new_state][aname]
                if (
                    ff_out == "charmm"
                    and oldresname in gromos2charmm
                    and new_state in gromos2charmm[oldresname]
                    and aname in gromos2charmm[oldresname][new_state]
                ):
                    aname = gromos2charmm[oldresname][new_state][aname]

            elif anumb not in other_atoms:
                continue

            if resnumb > TERMINAL_OFFSET:
                termini_resname = termini[chain][resnumb]
                resnumb -= TERMINAL_OFFSET
                if resnumb in resnumb_sites[chain]:
                    _, ter_new_state, resname, ter_removeHs = new_states[chain][resnumb]
                else:
                    resname = termini_resname
                # print(new_pdb_line(anumb, aname, resname, resnumb, x, y, z).strip())
            if chain in cys_bridges and resnumb in cys_bridges[chain]:
                resname = "CYX"
            resnumb_corrected = resnumb
            icode = " "
            if chain in renumbered and resnumb in renumbered[chain]:
                resnumb_corrected, icode = renumbered[chain][resnumb]
            counter += 1
            new_pdb += new_pdb_line(
                counter,
                aname,
                resname[:3],
                resnumb_corrected,
                x,
                y,
                z,
                chain=chain,
                icode=icode,
            )
            if chain in mainchain_Hs and resnumb in mainchain_Hs[chain]:
                while len(mainchain_Hs[chain][resnumb]) > 0:
                    counter += 1
                    (aname, anumb, oldresname, chain, x, y, z) = mainchain_Hs[chain][
                        resnumb
                    ].pop()
                    if (
                        resnumb not in in_delphi_pdb[chain]
                        or aname not in in_delphi_pdb[chain][resnumb]
                    ):
                        resnumb_corrected = resnumb
                        icode = " "
                        if chain in renumbered and resnumb in renumbered[chain]:
                            resnumb_corrected, icode = renumbered[chain][resnumb]
                        new_pdb += new_pdb_line(
                            counter,
                            aname,
                            resname[:3],
                            resnumb_corrected,
                            x,
                            y,
                            z,
                            chain=chain,
                            icode=icode,
                        )
                del mainchain_Hs[chain][resnumb]
        elif not line.startswith("ENDMDL"):
            new_pdb += line

    outputpqr = "leftovers.pqr"
    logfile = "LOG_pdb2pqr_nontitrating"
    if ff_out == "gromos_cph":
        ff_out = "GROMOS"
    mend_pdb(
        Config.pypka_params["pdb2pqr_inputfile"],
        outputpqr,
        ff_out,
        ff_out,
        logfile=logfile,
    )
    os.system("rm -f input_clean_fixed.pdb")

    with open(outputpqr) as f:
        for line in f:
            if line.startswith("ATOM "):
                (
                    aname,
                    anumb,
                    resname,
                    chain,
                    resnumb,
                    x,
                    y,
                    z,
                    charge,
                    radius,
                ) = read_pqr_line(line)
                if chain not in mainchain_Hs:
                    counter += 1
                    new_pdb += new_pdb_line(
                        counter, aname, resname, resnumb, x, y, z, chain=chain
                    )
    to_remove = (logfile, outputpqr, Config.pypka_params["pdb2pqr_inputfile"])
    for f in to_remove:
        os.remove(f)
    with open(outputname, "w") as f_new:
        f_new.write(new_pdb)
