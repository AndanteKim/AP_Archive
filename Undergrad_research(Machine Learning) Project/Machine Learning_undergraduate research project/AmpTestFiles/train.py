import os
from ase import Atoms, Atom, units
import ase.io
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

def train_amp(convergencecriteria,trainingsetname,maxtrainingattempts):
	#specify temperature for MD
	#set descriptor and method to train ASE calculator using AMP
	calc = Amp(descriptor=Gaussian(),
	model=NeuralNetwork(hiddenlayers=(10,10,10)),cores=1)
	#set convergence criteria for model
	calc.model.lossfunction.parameters['convergence'].update(convergencecriteria)
	#attempts to train the calculator to the training set
	#if it fails on the first attempt because too many steps were taken, continue training
	numberofattempts=1
	tic=0
	toc=0
	while numberofattempts <= maxtrainingattempts:
		try:
			if numberofattempts==1:
				print('training, attempt ',numberofattempts)					
				tic = time.time()
				#train using amp
				calc.train(images=trainingsetname)
				toc = time.time()
				print('training time', toc-tic)
			else:
				print('training, attempt ',numberofattempts)				
				tic = time.time()
				calc.model.lossfunction.parameters['convergence'].update(convergencecriteria)
				#train using amp, overwrite old file
				calc.train(overwrite=True, images=trainingsetname)
				toc = time.time()
				print('training time', toc-tic)
		except TrainingConvergenceError:
			numberofattempts+=1
			if numberofattempts > maxtrainingattempts:
				#append absurdly high value for error so that this point can be ignored when graphing
				return 'fail', calc
				break
			continue
		return 'success', calc
		break
