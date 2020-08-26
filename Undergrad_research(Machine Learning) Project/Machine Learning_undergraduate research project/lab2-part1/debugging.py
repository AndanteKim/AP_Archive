#!/usr/bin/env python

# This script is full of common errors you're likely to run into.
# To fix it, you need to debug it. Look at the error messages, use print
# statements, and trace your code by hand on paper to find and fix the bugs.


#----------------
import numpy

# This function is meant to count the number of 7's in an array  
def countSevens(data):
    count = 0
    for num in data:
        if num == 7 :
            count += 1
    return count

# This function is meant to return the percent of entries equal to 7 in an array  
def percentSevens(data):
    count = 0
    lengtharray = 0
    for num in data:
        if num == 7 :
            count += 1
        lengtharray += 1
    return float(count)/float(lengtharray) * 100

# This function is meant to return the sum of the values in an array. 
def totalSum(data):
    sum = 0
    for i in range(len(data)) :
        sum += data[i]
    return sum

cards = numpy.array([1, 3, 7, 11, 7, 2])
print 'Number of 7s:',countSevens(cards)
print 'Sum of values in array:', totalSum(cards)
print 'Percent 7s',percentSevens(cards)
