#import generate.py train.py and test.py to generate, train, and test nueral network
import generate
import train
import test

import os
from ase import Atoms, Atom, units
import ase.io
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import VelocityVerlet
from ase.constraints import FixAtoms
import tsase
import numpy as np
import sys
from amp import Amp
from amp.descriptor.gaussian import Gaussian
from amp.model.neuralnetwork import NeuralNetwork
from amp.utilities import TrainingConvergenceError
from amp.regression import Regressor
from scipy.optimize import basinhopping
import time

import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

###  NOTES  ###

#set what method is used to create training/testing sets (Options: 'random', 'optimization','MD')
trainingset='MD'
testset='MD'

#text for plot title and figure names
plottitleprefix = 'Trained and Tested with MD at '
plotfiguresuffix = 'LJ38_MD.png'


convergencecriteria = {'energy_maxresid': 0.01,
						'force_maxresid': None} #convergence criteria specifying highest acceptable error
maxtrainingattempts=5 #number of attempts to retrain
trainingstructure='lj3' #lj structure used to train
testingstructure='lj3' #lj structure used to test

trainingnumber=500 #number of data points for training
testingnumber=500 #number of data points for testing

trainingsetname='training.traj' #name of training set file
testingsetname='testing.traj' #name of testing set file

#if both onlytrainonce and onlycreatetestonce are 'yes' then it will create one graph showing the change the comparison of amp and LJ energies
onlytrainonce='yes' #if wanting to test different sets using the same calculator each time set to 'yes' otherwise set to 'no'
onlycreatetestonce='yes' #if wanting to test on the same training set every time, set to 'yes' otherwise set to 'no'

#parameters for generating optimization sets
inter=20 #atom positions written out to training/testing set every 'inter' steps
forcemax=0.01 #factor to scale forces
maxstep=0.1 #maximum allowed step size

#parameters for generating MD sets
temperature=2000 #temperature in Kelvin
timestep=0.01 #timestep in fs


####Main Function####

#add some global variables to generate.py
generate.trainingsetname = trainingsetname
generate.testingsetname = testingsetname
#call function in generate.py to create training sets
print('creating training set')
generate.create_train(trainingset,trainingsetname,trainingstructure,trainingnumber,inter,forcemax,maxstep,temperature,timestep)
print('training amp')
success, calc = train.train_amp(convergencecriteria,trainingsetname,maxtrainingattempts)
if success == 'fail':
	raise ValueError('Your optimization could not be successfully completed')
	#call function in generate.py to create testing set
print('creating test set')
generate.create_test(testset,testingsetname,testingstructure,testingnumber,inter,forcemax,maxstep,temperature,timestep)	
print('testing')
#call function from test.py to test amp, plot title included in function to create graph
mse = test.test_amp(calc,testingsetname,testingnumber,plottitleprefix+str(temperature),str(temperature)+plotfiguresuffix)
print('MSE', mse)
