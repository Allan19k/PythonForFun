from rdkit import Chem
from rdkit.Chem import Draw

moleculas = {
    "Agua": "O", # H2O, pero el SMILES para el agua es simplemente "O" porque el hidrógeno se asume implícitamente.
    "Metano": "C", # CH4, pero el SMILES para el metano es simplemente "C" porque los hidrógenos se asumen implícitamente.
    "Etanol": "CCO", # C2H5OH
    "Glucosa": "C(C1C(C(C(C(O1)O)O)O)O)O", # C6H12O6 
}
for nombre, smi in moleculas.items():
    mol = Chem.MolFromSmiles(smi)
    img = Draw.MolToImage(mol, size=(300, 300))
    img.show()

""" Representación Molecular (SMILES)

Las estructuras moleculares de este programa se definen mediante **SMILES (Simplified Molecular Input Line Entry System)**.


SMILES es una notación que representa estructuras químicas como cadenas de texto.

Por ejemplo:

- `"O"` representa el agua (H₂O), donde los átomos de hidrógeno son implícitos.
- `"C"` representa el metano (CH₄).
- Las moléculas más complejas, como la glucosa, se representan mediante:

    - paréntesis `()` para ramificaciones.
    - números para cierres de anillo.
    - átomos como C, O, N de forma explícita.

Esta codificación permite que bibliotecas como RDKit reconstruyan y visualicen estructuras moleculares mediante programación. """