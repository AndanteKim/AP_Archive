#import generate.py train.py and test.py to generate, train, and test neural network
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

def main_ML(temp,Method):
    ###  NOTES  ###

    #set what method is used to create training/testing sets (Options: 'random', 'optimization','MD')
    trainingset='MD'
    testset='MD'

    #text for plot title and figure names
    plottitleprefix = 'Trained and Tested with MD at '
    plotfiguresuffix = 'MD_'+Method+'_'+str(temp)+'.png'

    convergencecriteria = {'energy_maxresid': 0.05,
						'force_maxresid': None} #convergence criteria specifying highest acceptable error
    maxtrainingattempts=5 #number of attempts to retrain
    trainingstructure='../ML_AMP_Files/structures/lj5' #lj structure used to train
    testingstructure='../ML_AMP_Files/structures/lj5' #lj structure used to test

    trainingnumber=500 #number of data points for training
    testingnumber=500 #number of data points for testing

    trainingsetname=str(temp)+'.traj' #name of training set file
    testingsetname=str(temp)+'.traj' #name of testing set file

    #parameters for generating MD sets
    temperature=temp #temperature in Kelvin
    timestep=0.01 #timestep in fs

    ####Main Function####

    #if both onlytrainonce and onlycreatetestonce are 'yes' then it will create one$
    onlytrainonce='no' #if wanting to test different sets using the same calculato$
    onlycreatetestonce='no' #if wanting to test on the same training set every tim$

    #parameters for generating optimization sets
    inter=20 #atom positions written out to training/testing set every 'inter' steps
    forcemax=0.01 #factor to scale forces
    maxstep=0.1 #maximum allowed step size

    #add some global variables to generate.py
    generate.trainingsetname = trainingsetname
    generate.testingsetname = testingsetname
    
    #start a sign
    print(str(temperature)+'K Machine Learning starts')
    #call function in generate.py to create training sets as MD method
    print('creating training set as MD')
    generate.create_train(Method,trainingset,trainingsetname,trainingstructure,trainingnumber,inter,forcemax,maxstep,temperature,timestep)
    #call function in generate.py to create testing set as MD method
    #print 'creating test set as MD'
    #generate.create_test(testset,testingsetname,testingstructure,testingnumber,inter,forcemax,maxstep,temperature,timestep)
    #call funcation in generate.py to switch type from MD to optimization
    new_trainingset, new_testset = generate.switch_type(trainingset, testset)
    if new_trainingset != 'optimization' or new_testset != 'optimization':
        print('Switch failed. Program ended')
        sys.exit()
    #call function in generate.py to create training sets as optimization
    print('creating training set as optimization')
    generate.create_train(Method,new_trainingset,trainingsetname,trainingstructure,trainingnumber,inter,forcemax,maxstep,temperature,timestep)
    print('training amp')
    success, calc = train.train_amp(convergencecriteria,trainingsetname,maxtrainingattempts)
    if success == 'fail':
        raise ValueError('Your optimization could not be successfully completed')
    #call function in generate.py to create testing sets as optimization
    print('creating test set as optimization')
    generate.create_test(Method,new_testset,testingsetname,testingstructure,testingnumber,inter,forcemax,maxstep,temperature,timestep)	
    print('test result of optimization')
    #call function from sampletest.py to test LJ, plot title included in function to create graph
    test.test_amp(calc,testingsetname,testingnumber,plottitleprefix+str(temperature),str(temperature)+plotfiguresuffix)
