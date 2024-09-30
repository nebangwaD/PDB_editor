##  Python script for automatic PDB file editing – rename chain ID, re-number residues

Scipt 1: 'rename_pdb.py' is aimed at renaming and renumbering both chain ID and residue IDs of an input pdb file.

### Benefits
Key benefit include to resolve overlaping chain and residue numbering found in pdb files.

### Usage
1. Run the shell command "python rename_pdb.py" in same direcotry as input pdb file 
2. Tool then prompts for user input information including "input_file_name:", "chain_id:",and " start_residue_number:"
3. Final output saved as "edited_"input_file_name".pdb"
