from Bio.PDB import PDBParser, PDBIO

def rename_residues(pdb_file, chain_id, start_residue_number):
    parser = PDBParser()
    structure = parser.get_structure('structure', pdb_file)
    model = structure[0]
    
    for chain in model:
        if chain.id == chain_id:
            for i, residue in enumerate(chain):
                residue.id = (' ', start_residue_number + i, ' ')
    
    io = PDBIO()
    io.set_structure(structure)
    io.save(f'edited_{pdb_file}')

if __name__ == "__main__":
    pdb_file = input("Enter the PDB file name: ")
    chain_id = input("Enter the chain ID to edit: ")
    start_residue_number = int(input("Enter the starting residue number: "))
    rename_residues(pdb_file, chain_id, start_residue_number)
    print(f"Residues in chain {chain_id} have been renamed starting from {start_residue_number} and saved to edited_{pdb_file}")

