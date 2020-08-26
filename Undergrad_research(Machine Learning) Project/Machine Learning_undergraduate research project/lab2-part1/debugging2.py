#!/usr/bin/env python

# This script is full of common errors you're likely to run into.
# To fix it, you need to debug it. Look at the error messages, use print
# statements, and trace your code by hand on paper to find and fix the bugs.

# This scripts calculates the fibonacci sequence in four different ways. 
# Be sure to read the description at the top of each function.
# The goal is not to change the way in which the code is written but to find 
# all the semantic and syntax errors. 

#----------------
import numpy

# This function prints the first n numbers of the  fibonacci sequence 
#def print_n_fibonacci(n):
#    a = 1.
#    b = 1.
#    print a 
#    print b
#    counter = 2
#    for i in range(n):
#        newa = b
#        b = a+b
#        a = newa
#        print b
#        counter +=1
#    print 'This function requested ', n, 'numbers and printed ',counter,'numbers'

#print 'output for print_n_fibonacc where n =',10,':'
#print_n_fibonacci(10)
#print

# This function prints the fibonacci sequence up to the number 610 
#def print_fibonacci_upto610() : 
#    a,b = 1.,1.
#    print a
#    print b
#    while b < 610:
#        a,b = b,a+b
#        print b

#print 'output for print_fibonacci_upto610:'
#print_fibonacci_upto610()
#print

# This function creates a list which contains the first n numbers of the 
# fibonacci sequence and returns this list  
#def create_fibonacci_list_uptoN(n):
#    fibonacci = [1.,1.]
#    for i in range(n):
#        fibonacci.append(fibonacci[i]+fibonacci[i+1])
#    return fibonacci

#print 'list return from create_fibonacci_list_uptoN where n =',10,':'
#fib = create_fibonacci_list_uptoN(10)
#print fib
#print 'The length of the returned list is', len(fib)
#print

# This function creates a numpy array which contais the fibonacci sequence 
# up to the number 610
def create_fibonacci_array_upto610():
    counter = 1
    fibonacci = numpy.array([1.,1.])
    while fibonacci[counter] < 610. :         
        fibonacci = numpy.append(fibonacci, fibonacci[counter-1] + fibonacci[counter])
        counter += 1
    return fibonacci

print 'array return from create_fibonacci_array_upto610:'
fib = create_fibonacci_array_upto610()
print fib
