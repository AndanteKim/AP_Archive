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


def run_md(p,numdt, dt, mdinterval,T):
    f = p.get_forces()
    tsase.io.write_con('./structures/lj7_MD/movie_nvt.con',p,w='w')  # initiates a movie for the MD trajectory
    traj = ase.io.Trajectory('./structures/lj7_MD/2000.traj','w', p)
    opt = ase.optimize.FIRE(p,logfile=None,trajectory=traj,maxmove=0.2) #uctures/lj7_MD/2000.traj', maxmove=0.2)
    opt.attach(traj.write,interval=20)
    for i in range(1000):
        therm.apply_thermostat()
        f = step(p,dt,f)
    for i in range(int(numdt)):
        traj = ase.io.Trajectory('./structures/lj7_MD/'+str(T)+'.traj', 'w',p)
        therm.apply_thermostat()                 # apply the thermostat at each MD step
        f = step(p,dt,f)
        #print (i,p.get_potential_energy())
        # take an MD step
        if i%100 == 0:                           ### get snap shot for movie every 100 timesteps
            tsase.io.write_con('./structures/lj7_MD/movie_nvt.con',p,w='a')   # Append to movie of the MD trajectory
        if i%mdinterval == 0:
            holdpos = p.get_positions()
            #opt = tsase.optimize.SDLBFGS(p,logfile=None,maxstep=0.2)
            #traj = ase.io.Trajectory('./structures/lj7_MD/'+str(T)+'.traj','a', p)           
            #opt.attach(opt.trajectory,interval=20)
            opt.run(fmax=0.05)
            # add optimization  trajectory to training set in external file -- Andrew K
            p.set_positions(holdpos)
            traj.close()

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
    time = 1000.
    numdt = time/dt_fs# Set total time of the MD trajectory (Note: This trajectory is for 50,000 femtoseconds and will work for any timestep)
    run_md(p,numdt,dt,100,T)

sys.exit()
