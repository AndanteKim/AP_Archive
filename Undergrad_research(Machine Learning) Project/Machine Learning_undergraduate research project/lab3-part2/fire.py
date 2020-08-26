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
#p = tsase.io.read_con('diatomic.con')     ##lj38-clusters/0.con')
#p = tsase.io.read_con('lj38-clusters/0.con')

#### Define the PES ##########################################
#lj = tsase.calculators.lj(cutoff=3.5)
#p.center(50.0)
#p.set_calculator(lj)

#############################################################
## INSERT NEW CODE BELOW ################

def gradient_descent(a, con_cri) :
    maximumstep = 0.2
    #filename = 'movie.con'
    #tsase.io.write_con(filename,p,w='w')
    #tsase.io.write_con(filename,p,w='a')
    mag_vec = numpy.linalg.norm(p.get_forces())
    
    while numpy.linalg.norm(p.get_forces()) > con_cri :
        step = a * p.get_forces()
        mag_step = numpy.linalg.norm(step)
        if mag_step > maximumstep:
            nor_vec = maximumstep * step/mag_step # find the normal vector
            p.set_positions(p.get_positions() + nor_vec) # set out the new p positions
        else :
            p.set_positions(p.get_positions() + step)            
        #print 'new positions : ', p.get_positions()
        #print lj.force_calls, 'potential energy : ', p.get_potential_energy()
        #print '               forces :    ', numpy.linalg.norm(p.get_forces())
        #tsase.io.write_con(filename,p,w='a')
        if lj.force_calls == 10000 : break
        
    return p.get_potential_energy(), numpy.linalg.norm(step), p.get_positions()
    

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

a = 0.001
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
for i in range (0, 100) :
    p = tsase.io.read_con('lj38-clusters/'+str(i)+'.con')
    lj = tsase.calculators.lj(cutoff=3.5)
    p.center(50.0)
    p.set_calculator(lj)
    #p_e,vec,pos  = gradient_descent(a, convergence_criteria)
    #print str(i+1)+'. Final potential Energy :', p_e
    #print '   Final magnitude of vector :', vec
    #print '   Final position : '
    #print pos
    opt = ase.optimize.FIRE(p,logfile=None,maxmove = 0.2)
    opt.run(fmax=0.01)
sys.exit()








