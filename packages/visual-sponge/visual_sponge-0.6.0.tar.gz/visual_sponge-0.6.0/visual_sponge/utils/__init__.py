from MDAnalysis.analysis import distances

def guess_bonds(u, atoms, cutoff):
    others = u.select_atoms("not (resname WAT or resname HOH or resname H2O)")
    waters = u.select_atoms("resname WAT or resname HOH or resname H2O")
    other_distances = distances.distance_array(others, others)
    mask = other_distances < cutoff
    for i, atomi in enumerate(others):
        for j in range(i + 1, len(others)):
            if mask[i][j]:
                atoms[atomi.id - 1]["bonds"].append(int(others[j].id) - 1)
    for residue in waters.residues:
        for i, o in enumerate(residue.atoms):
            for j in range(i+1, len(residue.atoms)):
                h = residue.atoms[j]
                atoms[o.id - 1]["bonds"].append(int(h.id) - 1)
