import os
from ase import Atoms, Atom, units
import ase.io
from ase.calculators.emt import EMT
from ase.build import fcc110
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import VelocityVerlet
from ase.constraints import FixAtoms
import tsase
import numpy as np
import sys
from amp import Amp
from amp.descriptor.gaussian import Gaussian
from amp.descriptor.zernike import Zernike
from amp.model.neuralnetwork import NeuralNetwork
from amp.utilities import TrainingConvergenceError
from amp.regression import Regressor
from scipy.optimize import basinhopping
import time

import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

def switch_type(ori_train,ori_test) :
    #### switch type from MD to optimization
    ori_train, ori_test = 'optimization','optimization'
    return ori_train,ori_test

def reset_set(filename):
	#remove previously trained model if retraining or remove test set if generating new test set
	#trainingsetname and testingsetname are global variables
	if filename == trainingsetname:
		os.system("rm -r amp* ")#+filename)
	elif filename == testingsetname:
		os.system("rm "+filename)
	
	#create file to write atom positions to
	traj = ase.io.Trajectory(filename, 'w')
	#ensure that training and test sets use different random starting structures
	startnumb = 0
	if filename == testingsetname:
		startnumb=1	
	return traj, startnumb

def generate_data_optimization(filename,ljcluster,inter,forcemax,maxstep,numberofstructures):
	#create new testing/training set
	traj, startnumb = reset_set(filename)
	#loop through the 1000 available starting strucutres
	for i in range(startnumb,1000,1):
		lj = tsase.calculators.lj(cutoff=15.0)
		#read in randomly generated starting structure
		atoms = tsase.io.read_con('./structures/lj3_MD/'+str(i)+'.con')
		#ljcluster+'/'+str(i)+'.con')
		atoms.set_calculator(lj)
		atoms.get_potential_energy()
		#write out structures during optimization
		opt = ase.optimize.FIRE(atoms,maxmove = maxstep)
		traj = ase.io.Trajectory(filename, 'a',atoms)
		opt.attach(traj.write,interval=inter)
		opt.run(fmax=forcemax)
		traj.close()
		#stop producing structures when desired number is reached
		if len(traj)>numberofstructures:
			break
	
def generate_data_MD(filename,ljcluster,temperature,timestep,forcemax,maxstep,numberofstructures):
	#create new testing/training set
	traj, startnumb = reset_set(filename)
	#loop through the 1000 available starting strucutres
	lj = tsase.calculators.lj(cutoff=15.0)
	#read in randomly generated starting structure
	atoms = tsase.io.read_con(ljcluster+'/'+str(startnumb)+'.con')
	atoms.set_calculator(lj)
	atoms.get_potential_energy()
	#find optimum before starting MD
	opt = ase.optimize.FIRE(atoms,maxmove = maxstep)
	traj = ase.io.Trajectory(filename, 'a',atoms)
	opt.run(fmax=forcemax)
	MaxwellBoltzmannDistribution(atoms, temperature * units.kB)
	#set dynamics timestep
	dyn = VelocityVerlet(atoms, dt=timestep * units.fs)
	#run dynamics 
	for step in range(numberofstructures):
		dyn.run(100)
		traj.write(atoms)
                print(atoms.get_potential_energy())
		tsase.io.write_con('./structures/lj3_MD/'+str(step)+'.con',atoms,w='w')
		if len(traj)>numberofstructures:
			break

def generate_data_random(filename,ljcluster,numberofstructures):
	#create new testing/training set
	traj, startnumb = reset_set(filename)
	#loop through the 1000 available starting strucutres
	for i in range(startnumb,1000,2): #use even diatomics to train data
		lj = tsase.calculators.lj(cutoff=15.0)
		atoms = tsase.io.read_con(ljcluster+'/'+str(i)+'.con')
		atoms.set_calculator(lj)
		atoms.get_potential_energy()
		traj.write(atoms)
		if len(traj)>numberofstructures:
			break

#function to generate training set
def create_train(trainingset,trainingsetname,trainingstructure,trainingnumber,inter,forcemax,maxstep,temperature,timestep):
	if trainingset == 'optimization':
		generate_data_optimization(trainingsetname,trainingstructure,inter,forcemax,maxstep,trainingnumber)
	elif trainingset == 'MD':
		generate_data_MD(trainingsetname,trainingstructure,temperature,timestep,forcemax,maxstep,trainingnumber)
	elif trainingset == 'random':
		generate_data_random(trainingsetname,trainingstructure,trainingnumber)
	else:
		raise ValueError('Specify valid training set type')

#function to generate testing set
def create_test(testset,testingsetname,testingstructure,testingnumber,inter,forcemax,maxstep,temperature,timestep):
	if testset == 'optimization':
		generate_data_optimization(testingsetname,testingstructure,inter,forcemax,maxstep,testingnumber)
	elif testset == 'MD':
		generate_data_MD(testingsetname,testingstructure,temperature,timestep,forcemax,maxstep,testingnumber)
	elif testset == 'random':
		generate_data_random(testingsetname,testingstructure,testingnumber)
	else:
		raise ValueError('Specify valid testing set type')
