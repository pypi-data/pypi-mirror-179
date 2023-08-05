from pdbmender.formats import new_pdb_line, read_pdb_line, read_pqr_line
from pdbmender.utils import mend_pdb
from pdbmender.ffconverter import (
    AMBER_protomers,
    GROMOS_protomers,
    CHARMM_protomers,
    gromos2amber,
    gromos2charmm,
    mainchain_Hs,
)
import os


def getProtomerResname(
    pdb_content,
    pH,
    ff_protomers,
    resnumb,
    resname,
    most_prob_taut,
    state_prob,
    taut_prob,
    tit_curve,
    terminal_offset,
):
    new_state = most_prob_taut
    new_state_i = new_state - 1
    for ff_resname, protomers in ff_protomers[resname].items():
        if new_state_i in protomers.keys():
            new_resname = ff_resname
            remove_hs = protomers[new_state_i]
            average_prot = tit_curve[pH]
            if resnumb > terminal_offset:
                resnumb -= terminal_offset
            if state_prob < 0.75:
                warn = (
                    "{0}{1} "
                    "protonation state probability: {2}, "
                    "tautomer probability: {3}".format(
                        resname, resnumb, state_prob, taut_prob
                    )
                )
                print(warn)

            rounded_sprob = round(state_prob, 2)
            rounded_tprob = round(taut_prob, 2)
            rounded_avgprot = round(average_prot, 2)
            remark_line = (
                "{0: <5}{1: <6}    {2: >1.2f}         "
                "{3: >1.2f}         {4: >1.2f}".format(
                    resname,
                    resnumb,
                    rounded_avgprot,
                    rounded_sprob,
                    rounded_tprob,
                )
            )
            pdb_content += "REMARK     {text}\n".format(text=remark_line)
    # print(resnumb, new_state, new_resname, remove_hs, state_prob, taut_prob)
    return pdb_content, new_state_i, new_resname, remove_hs


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
    pdb2pqr_inputfile,
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
                terminal_offset,
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

            if resnumb > terminal_offset:
                termini_resname = termini[chain][resnumb]
                resnumb -= terminal_offset
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
        pdb2pqr_inputfile,
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
    to_remove = (logfile, outputpqr, pdb2pqr_inputfile)
    for f in to_remove:
        os.remove(f)
    with open(outputname, "w") as f_new:
        f_new.write(new_pdb)
