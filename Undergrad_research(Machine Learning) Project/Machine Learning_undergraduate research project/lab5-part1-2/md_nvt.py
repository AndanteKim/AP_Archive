#!/usr/bin/env python

import numpy
import sys
import matplotlib
matplotlib.use("agg") # Change to "agg" to run on FRI
from pylab import *
import tsase
import ase

##### Setting up the atoms object with ASE and TSASE #########
##############################################################

#### Import the starting structure from a file ###############
p = tsase.io.read_con('cluster_38.con')

#### Define the PES ##########################################
lj = tsase.calculators.lj(cutoff=35.0)
p.center(50.0)
p.set_calculator(lj)

###############################################################
#### MOLECULAR DYNAMICS #######################################
###############################################################

#### making trajectory graphic function #######
def plot_trajectory(tem_dt1, time_dt1) :
    figure()
    plot(time_dt1, tem_dt1,c='b',label='dev of time and PE')
    scatter(time_dt1, tem_dt1,c='r')  #  This will plot the points sam$
    #plot(time_dt2, total_energy_dt2,c='r',label='high kinetic energy')
    #scatter(time_dt2, total_energy_dt2,c='r')
    #ylim([-5,5])                 #  This specifies the range of the y-axis in $
    xlabel('time')
    ylabel('potential energy')
    title('the deviation for time and PE')
    legend(loc=2)
    savefig('time_devPE_300K.png')


#### a few important functions for MD  #####
#### VELOCITY-VERLET ALGORITHM ##############
def step(p,dt,f,fixcm=True):
    m = p.get_momenta()
    m += 0.5 * dt * f    
    if fixcm:
        msum = m.sum(axis=0) / float(len(m))
        m = m - msum
    p.set_positions(p.get_positions() + dt * m / p.get_masses()[:,numpy.newaxis])
    p.set_momenta(m)
    f = p.get_forces()
    p.set_momenta(p.get_momenta() + 0.5 * dt * f)
    return f

################################################################


def run_md(numdt, dt):
    devtem_array, Time = [], [] 
    Tem_Init = p.get_temperature()
    PE_Init = p.get_potential_energy()
    f = p.get_forces()
    tsase.io.write_con('movie_nvt300K.con',p,w='w')  # initiates a movie for the MD trajectory 
    for i in range(int(time)):
        therm.apply_thermostat()                 # apply the thermostat at each MD step
        f = step(p,dt,f)                         # take an MD step
        Time.append(i * 1.0) 
        if i%100 == 0:                           ### get snap shot for movie every 100 timesteps 
            tsase.io.write_con('movie_nvt300K.con',p,w='a')   # Append to movie of the MD trajectory
        devtem_array.append([p.get_potential_energy()])
    plot_trajectory(devtem_array, Time)

##### specify MD parameters (Note: In order to convert time into 
##### fs you need to multiple by ase.units.fs
T = 300.                     # Set the initial temperature, Original : 300K
dt_fs = 0.5                  # Set the initial time step for the MD simulations
dt = dt_fs * ase.units.fs    # Convert time step to correct units
kT = T * ase.units.kB        # Convert temperature to units of energy 


#### this is how to call the thermostat ########################
alpha = 0.8                  # Set Alpha for MD simulation
tcol = 100. * ase.units.fs   # Set tcol for MD simulations
therm = tsase.md.nvtandersen(p,dt,kT,alpha,tcol,fixcm=False)  # Call the thermostat from MD simulation

##### time of MD trajecotory in fs #############################
time = 50000.
numdt = time/dt_fs          # Set total time of the MD trajectory (Note: This trajectory is for 50,000 femtoseconds and will work for any timestep)
#print p.get_temperature()
run_md(numdt,dt)


sys.exit()








