import os
from ase import Atoms, Atom, units
import ase.io
import tsase
import numpy as np
import sys
from amp import Amp

import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

def test_amp(calc,testingsetname,testingnumber,plottitle,plotfigure):
	#creating array for energies calculated with LJ calculator
	lennardjones=[]
	#creating array for energies calculated with AMP calculator
	amppotential=[]
	#reads in testing set
	traj=ase.io.Trajectory(testingsetname, 'r')
	numb2=0
	for p in traj:
		#compare energies calculated by AMP calculator with those calculated by LJ calculator
		lj = tsase.calculators.lj(cutoff=15)
		p.center(50.0)
		p.set_calculator(lj)
		lennardjones.append(p.get_potential_energy())
		p.set_calculator(calc)
		amppotential.append(p.get_potential_energy())
		numb2=numb2+1
		#catch if more items in test set than intended
		if numb2 >=testingnumber:
			break
	traj.close()
	#calculate mean squared error and append to array
	mse=np.square(np.subtract(lennardjones, amppotential)).mean()
	#creates graph of Amp calculated energy and LJ calculated energy
	plt.figure()
	plt.scatter(lennardjones,amppotential)
	plt.xlabel('Energy Calculated using LJ Potential (eV)')
	plt.ylabel('Energy Calculated using AMP Potential (eV)')
	plt.title(plottitle)
	plt.savefig(plotfigure)
	return mse
