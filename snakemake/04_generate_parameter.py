"""
Acpype_params_gmx: Generation of topologies for GROMACS with ACPype
"""

import sys

from biobb_chemistry.acpype.acpype_params_gmx import acpype_params_gmx


ligandCode = 'IBP'
mol_charge = -1

if len(sys.argv) > 1:
	ligandCode = sys.argv[1]

if len(sys.argv) > 2:
	mol_charge = sys.argv[2]

# Create prop dict and inputs/outputs
output_babel_min = 'minimized/' + ligandCode + '.H.min.pdb'  

# Create prop dict and inputs/outputs
output_acpype_gro = 'parameters/' + ligandCode + '.params.gro'
output_acpype_itp = 'parameters/' + ligandCode + '.params.itp'
output_acpype_top = 'parameters/' + ligandCode + '.params.top'
output_acpype = ligandCode + 'params'
prop = {
    'basename' : output_acpype,
    'charge' : mol_charge
}

#Create and launch bb
acpype_params_gmx(input_path=output_babel_min,
                output_path_gro=output_acpype_gro,
                output_path_itp=output_acpype_itp,
                output_path_top=output_acpype_top,
                properties=prop)