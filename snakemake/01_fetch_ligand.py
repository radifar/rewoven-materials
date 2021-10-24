"""
Ligand: Download ligand structure from MMB PDB mirror REST API (https://mmb.irbbarcelona.org/api/)
"""

import sys

from biobb_io.api.ligand import ligand


ligandCode = 'IBP'

if len(sys.argv) > 1:
	ligandCode = sys.argv[1]

# Create prop dict and inputs/outputs
input_structure = 'ligands/' +ligandCode + '.pdb'

prop = {
    'ligand_code' : ligandCode
}

#Create and launch bb
ligand(output_pdb_path=input_structure,
        properties=prop)
