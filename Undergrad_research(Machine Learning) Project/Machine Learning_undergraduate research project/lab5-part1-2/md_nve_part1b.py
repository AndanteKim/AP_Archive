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
p = tsase.io.read_con('cluster_38_new.con')

#### Define the PES ##########################################
lj = tsase.calculators.lj(cutoff=35.0)
p.center(100.0)
p.set_calculator(lj)

#### Do a geometry optimization using the FIRE method  #######
dmin = ase.optimize.FIRE(p)
#dmin.run(fmax=0.01)

###############################################################
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
    p.set_positions(p.get_positions() + dt * m / p.get_masses()[:,numpy.newaxis])
    p.set_momenta(m)
    f = p.get_forces()
    p.set_momenta(p.get_momenta() + 0.5 * dt * f)
    return f

#### making trajectory graphic function #######
def plot_trajectory(total_energy_dt1, time_dt1) :
    figure()
    plot(time_dt1, total_energy_dt1,c='r',label='dev of time and temperature')     #  This will plot a line connecting all points
    scatter(time_dt1, total_energy_dt1,c='r')  #  This will plot the points sampled
    #plot(time_dt2, total_energy_dt2,c='r',label='high kinetic energy')
    #scatter(time_dt2, total_energy_dt2,c='r')    
    #ylim([-5,5])                 #  This specifies the range of the y-axis in $
    xlabel('time')
    ylabel('temperature')
    title('the deviation for temperature vs time')
    legend(loc=2)
    savefig('time_devtemperature_1000fs.png')

##### Function which runs MD for numdt timesteps (dt) ###########################

def run_md(numdt, dt):  # input variables are the number of timesteps (numdt) and the time step (dt) for your MD run 
    f = p.get_forces()
    newp = p
    newf = newp.get_forces()
    tsase.io.write_con('movie_nvt.con',p,w='w') # initiates a movie for the MD trajectory
    T = newp.get_total_energy()
    Temper_Init = p.get_temperature()
    T_init_e = p.get_total_energy()
    newT_init_e = newp.get_total_energy()
    T_e_array1, T_e_array2 = [], []
    Time_temper = []
    r_array = []
    f_array = []
    time1,time2 = [],[]
    print Temper_Init
    for i in range(int(numdt)+1):
        T_e_array2.append([p.get_total_energy() - T_init_e])
        r_array.append(numpy.linalg.norm(p.get_positions()))
        f_array.append(numpy.linalg.norm(p.get_forces()))
        Time_temper.append([p.get_temperature()- Temper_Init])
        time2.append(i*0.5)                       
        f = step(p,dt,f)        # take an MD step
    #newT_init_e = newp.get_total_energy()
    #for j in range (2 * int(numdt)+1):
    #    time1.append([j*1.0])
    #    T_e_array1.append([newp.get_total_energy() - newT_init_e])
    #    newf = step(newp,0.5 * dt,newf)                  
        if i%1 == 0:
            tsase.io.write_con('movie_nvt.con',p,w='a')  # Append to movie of the MD trajectory
    #print time1
    #print time2
    #print T_e_array1
    #print time2
    #plot_trajectory(T_e_array1, time1, T_e_array2, time2)
    #plot_trajectory(Time_temper, time2)    

################################################################
##### specify MD parameters (Note: In order to convert time into 
##### fs you need to multiple by ase.units.fs)


T = 300.                    # Set the initial temperature : origin - 300 K
dt_fs = 0.5                 # Set the initial time step for the MD simulations
dt = dt_fs * ase.units.fs   # Convert time step to correct units : ori - fs
kT = T * ase.units.kB       # Convert temperature to units of energy

#### get initial kinetic energy from the boltzmann distribution#
masses = p.get_masses()
vel = [[-numpy.sqrt(kT/masses[0]),0,0],[numpy.sqrt(kT/masses[0]),0,0]] # Set initial velocity; gives diatomic vibrational kinetic energy
#p.set_velocities(vel)
#print masses

##### time of MD trajecotory in fs #############################
time = 1000.0                   # Set total time of the MD trajectory (Note: This trajectory is for 20 femtoseconds )
numdt = time/dt_fs            # Convert time of the trajectory into numdt; Note that this will work for any time step!

# Call function to run MD
#p.set_masses(masses=[6.941,6.941]) # set hydrogen mole to increase total energy

#print p.get_total_energy()
#print p.get_kinetic_energy()
run_md(numdt,dt)

sys.exit()








