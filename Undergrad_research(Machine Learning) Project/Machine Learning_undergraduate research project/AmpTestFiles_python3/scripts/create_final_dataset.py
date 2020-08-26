"""This script removes all the configs with an extremely high force magnitude. Having outliers like that will negatively impact 
training of the neural network."""

from ase.io import read, write
from ase.io import Trajectory
import tsase
import numpy

# specify input and output files (.traj)
input_filename = 'lj8_carbon_4000-8000_3.traj'
output_filename = 'lj8_carbon_final.traj'

# read all the configs from the input trajectory. 
structures = read(input_filename, index = ':')
# open the output trajectory file for writing
traj = Trajectory(output_filename, 'w')
lj = tsase.calculators.lj(cutoff = 15.0)
# iterate over all the configs. 
for structure in structures:
    # set the configs calculator to get the forces.
    structure.set_calculator(lj)
    # calculate the force magnitude.
    force_mag = numpy.linalg.norm(structure.get_forces())
    # only write configs that are below a certain threshold to the final trajectory file. 
    if force_mag < 100:
        traj.write(structure) 
