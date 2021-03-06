#!/usr/bin/env python

### importing important libraries 
import numpy as np
import sys
import matplotlib
import math
from sympy import Symbol, Derivative
matplotlib.use("agg") # Change to "agg" to run on FRI
from pylab import *

###### Lennard-Jones Potential ################
###### The function below returns the potential energy for a given bond length (r), sigma and epsilon
def LJ(r,sigma,epsilon):
    Vlj = 4* epsilon * ( np.power(sigma/r,12) - np.power(sigma/r,6) )
    return Vlj

##### This function creates an array of various bond lengths (rarray) 
##### and its corresponding energy (energyarray)
##### this is required to plot the potential
def get_energy_array(rmin,rmax,numbersamples,sigma,epsilon):
    rarray = np.linspace(rmin,rmax,numbersamples)
    engarray = np.zeros(int(numbersamples))
    for i in range(len(rarray)):
        engarray[i] = LJ(rarray[i],sigma,epsilon)
    return engarray,rarray ## Note: python can return as many variables as you would like from a functions
                           ## Just seperate the output by a comma 

    
# The function below plots how the potential energy changes with bondlength using matplotlib 
# Try commenting out the plot and scatter functions below to see how they are different! 
def plot_pes(energyar,rar,filename):
    figure()
    plot(rar,energyar)     #  This will plot a line connecting all points
    scatter(rar,energyar)  #  This will plot the points sampled
    ylim([-5,5])                 #  This specifies the range of the y-axis in your plot; adjust as needed
    xlabel('Bond Length')
    ylabel('Potential Energy')
    title('Lennard-Jones potential for diatomic')
    savefig(filename)      # This is how you generate an output file which stores the image you are creating.
#  filename should be a string with an extension like '.png' or '.eps' (image file extensions) 

# Below will be the main part of the function where you run the functions required to do your computations
# The script is currently setup to create your energy and bondlengths arrays and 
# then plot the PES with an output file 'LJ_s1_e1.png

###### This is the formula of force ###############
def force(radius):
    r = Symbol('r')
    epsilon = 1.0
    sigma = 1.0
    formula = Derivative(-4 * epsilon * ( np.power(sigma/r,12) - np.power(sigma/r,6) ), r)
    #print 'Lennard-Jones Potential Formula : ', formula.doit()
    result = formula.doit().subs({r:radius})
    return result

######## This is gradient_decent function ##############################
def gradient_decent(r, alpha, convergence_criteria):
    step_array, vector_force, mag_force, LJ_array, r_array = [],[],[],[],[]
    step = 1
    step_array.append(step)    
    sigma, epsilon = 1.0, 1.0
    vector_force.append(force(r))
    mag_force.append(math.fabs(vector_force[step-1]))
    LJ_array.append(LJ(r, sigma, epsilon))
    r_array.append(r)
    while (mag_force[step-1] > convergence_criteria) :
        r = r + vector_force[step-1] * alpha
        step = step + 1
        step_array.append(step)
        vector_force.append(force(r))
        mag_force.append(math.fabs(vector_force[step-1]))
        LJ_array.append(LJ(r, sigma, epsilon))
        r_array.append(r)
                       
    return step_array, vector_force, mag_force, LJ_array, r_array    

####### This is plot_trajectory function #######

def plot_trajectory(sub_a, step_a, yaxis, name, SaveFile) :
    figure()
    plot(step_a, sub_a)     #  This will plot a line connecting all points
    scatter(step_a, sub_a)  #  This will plot the points sampled
    #ylim([-5,5])                 #  This specifies the range of the y-axis in y$
    xlabel('step number')
    ylabel(yaxis)
    title(name)
    savefig(SaveFile) 
# reminder of variables: rmin,rmax,numbersamples,sigma,epsilon
#energyarray,rarray = get_energy_array(0.5, 10., 300.0, 1., 1.)  ## Note: since this function returns two values 
                                                                ## there are two variable names for each returned value.
#plot_pes(energyarray,rarray,'LJ_s1_e1.png')
#energyarray,rarray = get_energy_array(0.5, 10., 300.0, 1., 5.)
#plot_pes(energyarray,rarray,'LJ_s1_e5.png')
#energyarray,rarray = get_energy_array(0.5, 10., 300.0, 5., 1.)
#plot_pes(energyarray,rarray,'LJ_s5_e1.png')
#energyarray,rarray = get_energy_array(0.5, 10., 300.0, 5., 5.)
#plot_pes(energyarray,rarray,'LJ_s5_e5.png')

step, v_f, m_f, p_e, b_len = gradient_decent(0.95, 0.005, 0.01)
#plot_trajectory(v_f, step,'force vector', 'Step Number and Force Vector correlation', 'stepvforce_alpha0.005.png')
#plot_trajectory(m_f, step,'magnitude vector', 'Step Number and Magnitude correlation', 'stepmforce_alpha0.005.png' )
#plot_trajectory(p_e, step, 'potential energy', 'Step Number and Potential Energy', 'stepPoEner_alpha0.005.png')
#plot_trajectory(b_len, step, 'bond length', 'Step Number and Bond Length', 'stepBoLen_alpha0.005.png')
 
#print "Steps : ", step
#print "Vector Force : ", v_f
#print "The Magnitude of Force : ", m_f
#print ", potential energy :", p_e
#print ", bondlength : ", b_len

step, v_f, m_f, p_e, b_len = gradient_decent(0.95, 0.009, 0.01)
#print "Steps : ", step
print "Vector Force : ", v_f
#print " the Magnitude of Force : ", m_f
#print ", final potential energy :", p_e
#print ", final bondlength : ", b_len
#plot_trajectory(v_f, step,'force vector', 'Step Number and Force Vector correlation', 'stepvforce_alpha0.001.png')
#plot_trajectory(m_f, step,'magnitude vector', 'Step Number and Magnitude correlation', 'stepmforce_alpha0.001.png')
#plot_trajectory(p_e, step, 'potential energy', 'Step Number and Potential Energy', 'stepPoEner_alpha0.001.png')
#plot_trajectory(b_len, step, 'bond length', 'Step Number and Bond Length', 'stepBoLen_alpha0.001.png')

#step, v_f, m_f, p_e, b_len = gradient_decent(0.95, 0.009, 0.01)
#plot_trajectory(v_f, step,'force vector', 'Step Number and Force Vector correlation', 'stepvforce_alpha0.009.png')
#plot_trajectory(m_f, step,'magnitude vector', 'Step Number and Magnitude correlation', 'stepmforce_alpha0.009.png')
#plot_trajectory(p_e, step, 'potential energy', 'Step Number and Potential Energy', 'stepPoEner_alpha0.009.png')
#plot_trajectory(b_len, step, 'bond length', 'Step Number and Bond Length', 'stepBoLen_alpha0.009.png')
