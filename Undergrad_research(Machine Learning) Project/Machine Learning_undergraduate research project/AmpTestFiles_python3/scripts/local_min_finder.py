""" This script creates logs of using FIRE to optimize structure. Provides an idea of the distribution of energies you would obtain when using 
optimization to create a training set (have to use another script to process all the logs) """

import ase
from ase.io import read
from ase.optimize.fire import FIRE
import tsase
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def get_local_mins(atoms_file):
    """ This function optimizes all the structures in the input file. returns a list of the initial energies and a list of the local mins obtained. """
    initial_energy_array = []
    local_min_array = []
    # obtain a lennard jones calculator.     
    lj_calc = tsase.calculators.lj(cutoff = 15.0)
    # read all the configs in the trajectory file. 
    structs = read(atoms_file, index = ':')
    atom_index = 0
    cellsize = 15
    # iterate over all the configurations. 
    for struct in structs:
        struct.set_cell([[cellsize, 0, 0], [0, cellsize, 0], [0, 0, cellsize]], scale_atoms=False)
        struct.set_pbc((True, True, True))
        struct.center()
        struct.set_calculator(lj_calc)
        initial_energy_array.append(struct.get_potential_energy())
        # run FIRE on the structure, a log file will automatically be created. 
        opt = FIRE(atoms = struct, maxmove = 1, dt = 0.2, dtmax = 1.0, logfile = 'log_'+str(atom_index))
        opt.run(fmax = 0.02)
        local_min_array.append(struct.get_potential_energy())
        atom_index = atom_index + 1
    return initial_energy_array, local_min_array

def plot(initial_energy, local_min):
    # This function plots a scatter plot with x,y pairs = initial_energy, local_min
    plt.figure()
    plt.scatter(initial_energy, local_min)
    plt.savefig('carbon.png')
    
i_energy, lmin = get_local_mins('test_carbon_4000-8000_sqrt_3.traj')
plot(i_energy, lmin)
