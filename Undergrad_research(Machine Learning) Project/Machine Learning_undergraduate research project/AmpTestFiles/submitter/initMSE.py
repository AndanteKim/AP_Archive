#!/usr/bin/env python
import os
import shutil

from tempfile import mkstemp
from shutil import move
from os import remove
import sys

def replace(source_file_path, pattern, substring): #replace lines with matching pattern with$
    f = open(source_file_path,'r')
    lines = f.readlines()
    f.close()
    num_lines = sum(1 for line in open(source_file_path))
    for i in range (num_lines):
        if pattern in lines[i]:
            lines[i] = substring+ '\n'
    f = open(source_file_path, 'w')
    f.write("".join(lines))
    f.close()

timesteparray=[0.1,0.2,0.3,0.4,0.5] #parameters to be looped through
os.mkdir('testrun') #makes a directory to contain test
os.chdir('testrun')	#changes current directory to be testrun
for i in timesteparray:
	directoryname=str(i).replace('.','_')#make a directory name from the parameter given
	os.mkdir(directoryname) #make directory for specific parameter
	os.chdir(directoryname) #change into that directory
	for files in ['generate.py','test.py','train.py','pylab1.sub','runamp.py']:
		shutil.copyfile('../../startingfiles/'+files,files) #copy over files starting files into directory
	shutil.copytree('../../structures/lj3','lj3')
	replace('pylab1.sub', '#$ -N Jobname', '#$ -N LJ'+directoryname) #replaces name of job to submit 
	replace('runamp.py','timestep=0.01','timestep='+str(i)) #replace line specifying parameter	
	os.system('qsub pylab1.sub') #submit job to queue
	os.chdir('..') #go one directory back
os.chdir('..')
