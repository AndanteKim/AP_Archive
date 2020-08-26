#!/usr/bin/env python

###################################################################################
# Python has many built-in functions and helpful modules for perfoming computations 
###################################################################################

# You have already seen a the following function, type:
print '32 is a', type(32)

# Here are a few other built in functions which will convert values from one type to another

string32 = '32'
print 'int converts the string 32 into an', 
integer32 = int(string32)
print type(integer32)

print 'str converts the integer 32 into a',    
string32 = str(integer32)
print type(string32)

print 'float converts the integer 32 into a',
float32 = float(integer32)
print type(float32)

# Python also has many useful modules with built functions for doing computations
# First, we will need import the numpy and math modules so that its tools can be used in the 
# python script. Below are two common ways of importing modules. Always import at the top of your script.

# One: Just importing the module. You would refer to it by its full name. 
import numpy
import math

# Two: Importing the module as another name. You would refer to it by this shorter name.
import numpy as np 

# Here are a few examples of helpful functions in these modules

print 'The square root of', 25., 'is', math.sqrt(25.)
print 'The square root of', 25., 'is', np.sqrt(25.)
print 'e^5 is', math.exp(5.)
print 'log(5) is',numpy.log(5.)
print '5 raised tot he 7th power is', numpy.power(5.,7.)

# This is just a few examples of the tools numpy and math has available. 
# We will continue to introduce other built in functions and modules throughout the semester.
# Google also has a lot of information! 

# For more information on numpy's useful functions, check out the documentation here
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#basic-operations
# or just try googling numpy and the name math operation you are interested in!
