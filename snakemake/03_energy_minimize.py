"""
Babel_minimize: Structure energy minimization of a small molecule after being modified adding hydrogen atoms
"""

import sys

from biobb_chemistry.babelm.babel_minimize import babel_minimize


ligandCode = 'IBP'

if len(sys.argv) > 1:
	ligandCode = sys.argv[1]

# Create prop dict and inputs/outputs
output_babel_h = 'protonated/' + ligandCode + '.H.mol2' 
output_babel_min = 'minimized/' + ligandCode + '.H.min.pdb'                              
prop = {
    'method' : 'sd',
    'criteria' : '1e-10',
    'force_field' : 'GAFF'
}


#Create and launch bb
babel_minimize(input_path=output_babel_h,
              output_path=output_babel_min,
              properties=prop)