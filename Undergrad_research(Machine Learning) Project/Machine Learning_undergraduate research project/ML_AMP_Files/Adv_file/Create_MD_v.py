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
#from amp import Amp
#from amp.descriptor.gaussian import Gaussian
#from amp.model.neuralnetwork import NeuralNetwork
##from amp.utilities import TrainingConvergenceError
from amp.regression import Regressor
from scipy.optimize import basinhopping
import time
#import train
import sampletest

#import matplotlib
#matplotlib.use("agg")
import matplotlib.pyplot as plt

print ('running')
##### Setting up the atoms object with ASE and TSASE #########
##############################################################
###############################################################
#### MOLECULAR DYNAMICS #######################################
###############################################################

#### a few important functions for MD  #####
#### VELOCITY-VERLET ALGORITHM ##############
def step(p,dt,f,fixcm=True):
    m = p.get_momenta()
    m += 0.5 * dt * f
    if fixcm:
        msum = m.sum(axis=0) / float(len(m))
        m = m - msum
    p.set_positions(p.get_positions() + dt * m / p.get_masses()[:,np.newaxis])
    p.set_momenta(m)
    f = p.get_forces()
    p.set_momenta(p.get_momenta() + 0.5 * dt * f)
    return f

################################################################

def opt_cluster(opt,p,cc,optinterval,writer,maxoptsteps):
    print('enter optimization')
    steps = 0
    while np.sqrt((p.get_forces()**2).sum(axis=1).max()) > cc:
        steps += optinterval
        print('run opt')
        opt.run(fmax=cc,steps=optinterval)
        writer.write(p,mode='a')
        print ('current forces:',np.sqrt((p.get_forces()**2).sum(axis=1).max()))
        optinterval += optinterval
        if steps > maxoptsteps:
            print('did not converge in allotted steps; current forces=',np.sqrt((p.get_forces()**2).sum(axis=1).max()))
            break

def run_md(p,numdt, dt, mdinterval,T):
    f = p.get_forces()
    tsase.io.write_con('./structures/lj7_MD/movie_nvt.con',p,w='w')  # initiates a movie for the MD trajectory
    opt = ase.optimize.FIRE(p,maxmove=0.2) #uctures/lj7_MD/2000.traj', maxmove=0.2)
    writer = ase.io.trajectory.TrajectoryWriter('./structures/lj7_MD/2000.traj',mode='w',atoms=p)
    for i in range(1000):
        therm.apply_thermostat()
        f = step(p,dt,f)
    for i in range(int(numdt)):
        therm.apply_thermostat()                 # apply the thermostat at each MD step
        f = step(p,dt,f)
        if i%100 == 0:                           ### get snap shot for movie every 100 timesteps
            tsase.io.write_con('./structures/lj7_MD/movie_nvt.con',p,w='a')   # Append to movie of the MD trajectory
        if i%mdinterval == 0:
            holdpos = p.get_positions()
            opt = ase.optimize.FIRE(p,maxmove=0.2) 
            opt_cluster(opt,p,0.05,20,writer,1000)
            p.set_positions(holdpos)        

#### Import the starting structure from a file ###############
for i in range(0, 1):
    p = tsase.io.read_con('./structures/lj7_MD/'+str(i)+'.con')
    print (' in for loop')
    #### Define the PES ##########################################
    lj = tsase.calculators.lj(cutoff=35.0)
    p.center(50.0)
    p.set_calculator(lj)

    ##### specify MD parameters (Note: In order to convert time into
    ##### fs you need to multiple by ase.units.fs
    T = 2000.                     # Set the initial temperature
    dt_fs = 0.5                  # Set the initial time step for the MD simulations
    dt = dt_fs * ase.units.fs    # Convert time step to correct units
    kT = T * ase.units.kB        # Convert temperature to units of energy

    #### this is how to call the thermostat ########################
    alpha = 0.8                  # Set Alpha for MD simulation
    tcol = 100. * ase.units.fs   # Set tcol for MD simulations
    therm = tsase.md.nvtandersen(p,dt,kT,alpha,tcol,fixcm=False)  # Call the thermostat from MD simulation

    ##### time of MD trajecotory in fs #############################
    time = 100.
    numdt = time/dt_fs# Set total time of the MD trajectory (Note: This trajectory is for 50,000 femtoseconds and will work for any timestep)
    run_md(p,numdt,dt,30,T)
    print('MD Optimization is done, and Ploting starts!')
    sampletest.test_amp('./structures/lj7_MD/2000.traj',500,'test','Training_2000K.png')
    print('2000K ended, and go to the next high temperature')
sys.exit()
