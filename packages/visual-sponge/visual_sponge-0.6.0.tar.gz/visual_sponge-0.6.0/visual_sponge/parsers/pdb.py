from pathlib import Path

from . import Parser
from .. import Model, mda
from ..utils import guess_bonds

class PDBParser(Parser, formats="pdb"):
    @staticmethod
    def Model_Parse(m, **kwargs):
        u = mda.Universe(m, topology_format="PDB", **kwargs)
        if hasattr(u.atoms, "elements"):
            atoms = [{"elem": atom.element,
                      "atom": atom.name,
                      "resi": int(atom.resid),
                      "resn": atom.resname,
                      "x": float(atom.position[0]),
                      "y": float(atom.position[1]),
                      "z": float(atom.position[2]),
                      "bonds":[]} for atom in u.atoms]
        else:
            atoms = [{"elem": atom.name[0],
                      "atom": atom.name,
                      "resi": int(atom.resid),
                      "resn": atom.resname,
                      "x": float(atom.position[0]),
                      "y": float(atom.position[1]),
                      "z": float(atom.position[2]),
                      "bonds":[]} for atom in u.atoms]
        guess_bonds(u, atoms, 1.6)
        model = Model(name=Path(m).stem, u=u)
        model.traj_files.append((m, "PDB"))
        return atoms, model

    @staticmethod
    def Traj_Parse(traj):
        return "PDB"
