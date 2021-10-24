"""
Babel_add_hydrogens: add Hydrogen atoms to a small molecule
"""

import sys

from biobb_chemistry.babelm.babel_add_hydrogens import babel_add_hydrogens


ligandCode = 'IBP'
pH = 7.4

print(sys.argv)

if len(sys.argv) > 1:
	ligandCode = sys.argv[1]

if len(sys.argv) > 2:
	pH = float(sys.argv[2])

input_structure = 'ligands/' + ligandCode + '.pdb'

# Create prop dict and inputs/outputs
output_babel_h = 'protonated/' + ligandCode + '.H.mol2' 

prop = {
    'ph' : pH,
    'input_format' : 'pdb',
    'output_format' : 'mol2'
}

#Create and launch bb
babel_add_hydrogens(input_path=input_structure,
                  output_path=output_babel_h,
                  properties=prop)