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


convergencecriteria = {'energy_maxresid': 0.05,
						'force_maxresid': None} #convergence criteria specifying highest acceptable error
maxtrainingattempts=5 #number of attempts to retrain
trainingstructure='structures/lj7' #lj structure used to train
testingstructure='structures/lj7' #lj structure used to test

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


msearray=[]
#array to loop through
temperaturearray=[100]

#loop through parameter to test effect (in this example temperature)
trainagain = 'yes'
createtestagain = 'yes'
for i in temperaturearray:
	print(i)
	#if training set should remain unchanged, don't change it
	if trainagain == 'yes':	
		#add some global variables to generate.py
		generate.trainingsetname = trainingsetname
		generate.testingsetname = testingsetname
		#call function in generate.py to create training sets
		generate.create_train(trainingset,trainingsetname,trainingstructure,trainingnumber,inter,forcemax,maxstep,temperature,timestep)
		success, calc = train.train_amp(convergencecriteria,trainingsetname,maxtrainingattempts)
		if success == 'fail':
			#if training fails append high value to sort data
			msearray.append(10000)
			if onlytrainonce == 'yes':
				trainagain = 'no'
			#move to next temp to train
			continue
	#if you only need to train the program once, only do it once
	if onlytrainonce == 'yes':
		trainagain = 'no'
	#create testing set
	if createtestagain == 'yes':	
		print('creating test')
		#call function in generate.py to create testing set
		generate.create_test(testset,testingsetname,testingstructure,testingnumber,inter,forcemax,maxstep,temperature,timestep)	
	#if you only need to create the test set once, only do it once
	if onlycreatetestonce == 'yes':
		createtestagain = 'no'
	print('testing')
	#call function from test.py to test amp
	mse = test.test_amp(calc,testingsetname,testingnumber,plottitleprefix+str(temperature),str(temperature)+plotfiguresuffix)
	msearray.append(mse)
	print('MSE', mse)

#exits out of the program if only one training and one testing set was used
if onlytrainonce == 'yes' and onlycreatetestonce == 'yes':
	sys.exit()

#if looped through multiple things, plot how it changes
#convert to numpy array
temparray=np.array(temperaturearray)
msearray=np.array(msearray)

#remove points where training failed
temparray = temparray[msearray < 1000.0]
msearray = msearray[msearray < 1000.0]

#plot the error vs. the temperature
plt.figure()
plt.scatter(temparray,msearray)
plt.xlabel('Temperature')
plt.ylabel('Mean Squared Error')
plt.title(plottitle+'Multiple Temperatures')
plt.savefig('../ML_AMP_Files/Mult_Temp'+plotfiguresuffix)
