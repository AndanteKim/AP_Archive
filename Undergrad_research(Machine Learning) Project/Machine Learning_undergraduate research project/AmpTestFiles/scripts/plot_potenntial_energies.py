
""" This script plots the distribution of energies in a training set. It requires a .traj file."""

import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
from ase.io import read
import tsase
import numpy 

def get_energies(filename):
    """ This function reads all the configurations in the traj file and returns all the energies"""
    # create an instance of a lj calculator
    lj = tsase.calculators.lj(cutoff = 15.0)
    # read the traj file, uses ase.io.read. index = ':' denotes read all configs. it is set to read only the last config by default.
    structures = read(filename, index = ':')
    pe_array = []
    i = 0
    # iterate over all the configs
    for structure in structures:
        # set the configs calculator to lj and get the potential energy and forces. 
        structure.set_calculator(lj)
        pe_lj = structure.get_potential_energy()
        force_vector = structure.get_forces()
        # get the force magnitude.
        force_mag = numpy.linalg.norm(force_vector)
        # based on the structure, ignore configs with a force magnitude above a certain level. 
        if force_mag < 100:
            pe_array.append(pe_lj)
            if pe_lj > 0:
                print(pe_lj)
        else:
            print('force_lj: {}, energy_lj: {}, index: {}'.format(numpy.linalg.norm(force_mag) ,pe_lj, i))
        i = i + 1 
    return pe_array

def plot(pe_array):
    """This function creates a histogram of the energies."""
    plt.figure()
    # supply the energy array to plt.hist() function. The function automatically scales the graph appropriately 
    plt.hist(pe_array)
    plt.savefig('4000-8000_3.png')

pe_array = get_energies('lj8_carbon_4000-8000_3.traj')
plot(pe_array)
