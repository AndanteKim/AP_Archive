#!/usr/bin/env python

###############################################################################
# Numpy is a Python module that allows us to use arrays, and do useful operations on them
###############################################################################

# First, we will need import the numpy module so that its tools can be used in the 
# python script. Below are two common ways of importing modules. Always import at the top.

# One: Just importing the module. You would refer to it by its full name. 
import numpy

# Two: Importing the module as another name. You would refer to it by this shorter name.
import numpy as np 


# The central feature of numpy is the array. These are similar to lists in python, 
# but every element needs to be of the same type. Creating arrays over lists will 
# make your code more efficient when doing numerical calculations. 

# This is how you would create an array by specifying the values. It is a numpy function,
# so you call it by first referring to numpy or np, depending on the import used
lowTemps = numpy.array([83,76,75,82,87,85,79])
print 'Array of low temperatures: ', lowTemps

# This is how you would create an array by specifying values and defining the type. 
# Inlcuding float changes all of the integer elements to floats
highTemps = numpy.array([97,98,99,100,101,102,103], int)
print 'Array of high temperatures: ', highTemps
grades = np.array([89, 93, 79, 94, 97],float) 
print 'Array of grades: ', grades

# You can also specify the size of a new array and fill it with either zeros or ones
# This is useful when you know the size of your array, but don't have values yet
sevenOnes = numpy.ones(7)
print 'numpy.ones(7): '
print sevenOnes

# This can be done in multiple dimensions, similar to matrices we discussed previously.
zerosSquare = np.zeros((3, 3))
print 'np.zeros((3,3)): '
print zerosSquare

# Arrays can be treated just like lists, when indexing and looping over them. 
print 'highTemps[1]: ', highTemps[1]

# You can add and subtract arrays, like matrices or vectors in math
temperatureRange = highTemps - lowTemps
print 'Temperature ranges for the week:',  temperatureRange

# Arrays can also be multiplied by a scalar, again like matrices or vectors in math
halvedGrades = 0.5 * grades
print '0.5 * grades: ', halvedGrades

# Thre other useful numpy functions are vdot (taking the dot product of two vectors), mean, linspace
print 'Dot product of highTemp and lowTemp: ', numpy.vdot(highTemps, lowTemps)
print 'Average grade: ', numpy.mean(grades)
minval = 0
maxval = 2
lengtharray = 3
print 'evenly spaced numbered array', numpy.linspace(minval,maxval,lengtharray)

# For more information on numpy's useful functions, check out the documentation here
# https://docs.scipy.org/doc/numpy/user/quickstart.html
# or just try googling numpy and the name math operation you are interested in! 
