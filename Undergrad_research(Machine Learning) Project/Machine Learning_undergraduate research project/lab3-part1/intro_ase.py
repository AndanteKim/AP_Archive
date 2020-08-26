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
p = tsase.io.read_con('diatomic.con')     ##lj38-clusters/0.con')

#### Define the PES ##########################################
lj = tsase.calculators.lj(cutoff=3.5)
p.center(50.0)
p.set_calculator(lj)

#############################################################
## INSERT NEW CODE BELOW ################

def gradient_descent(a, con_cri) :
    #p = tsase.io.read_con('diatomic.con')
    #lj = tsase.calculators.lj(cutoff = 3.5)
    #p.center(50.0)
    #p.set_calculator(lj)
    maximumstep = 0.2
    filename = 'movie.con'
    tsase.io.write_con(filename,p,w='w')
    tsase.io.write_con(filename,p,w='a')
    mag_vec = numpy.linalg.norm(p.get_forces())
    while mag_vec > con_cri :
        if mag_vec > maximumstep :
            Force = a * p.get_forces()     # find the maximum step of forces
            nor_vec = maximumstep * Force/mag_vec # find the normal vector
            shift_p = p.get_positions() + nor_vec # ready for setting new p positions
            p.set_positions(shift_p) # set out the new p positions
            mag_vec = numpy.linalg.norm(p.get_forces()) # find the magnitude the new p forces
        else :
            Force = a * p.get_forces()
            shift_p = p.get_positions() + Force
            p.set_positions(shift_p)
            mag_vec = numpy.linalg.norm(p.get_forces())            
        #print 'new positions : ', p.get_positions()
        print 'potential energy : ', p.get_potential_energy(), 'forces : ', mag_vec
        tsase.io.write_con(filename,p,w='a')
    #return p.get_positions()
    

#print 'positions : '
#print p.get_positions()
#print 'potential energy : '
#print p.get_potential_energy()
#print 'forces : '
#print p.get_forces()
#print 'distance : '
#print p.get_all_distances()
#newp = p.get_positions()
#newp[0][0] += 0.5
#p.set_positions(newp)
#print 'Before positions : '
#print p.get_positions()
#print 'Before potential energy : '
#print p.get_potential_energy()
#print 'Before forces : '
#print p.get_forces()

a = 0.005
convergence_criteria = 0.01
#Shift_p = p.get_positions() + a * p.get_forces()
#p.set_positions(Shift_p)
#print 'After positions : '
#print p.get_positions()
#print 'After potential energy : '
#print p.get_potential_energy()
#print 'After forces : '
#print p.get_forces()
#print 'Final normal vector : '

gradient_descent(a, convergence_criteria)

sys.exit()








