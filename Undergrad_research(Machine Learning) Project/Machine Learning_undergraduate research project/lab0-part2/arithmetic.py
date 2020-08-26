#!/usr/bin/env python

# Below are the options for basic arithmetic with python
# These can be done with numbers or variables

# Addition
print '2 + 4 = ', 2 + 4

# Subtraction
print '8 - 2 = ', 8 - 2

# Multiplication
print '4.0 * 2.1 = ', 4.0 * 2.1

# Remainder
10 % 4 
print 'The remainder of 10 divided by 4 is', 10 % 4 

# Integer Division: Returns an integer (truncates the remainder)
print '10 / 4 = ', 10 / 4

# Float Division: Returns a float (includes the remainder)
print '10.0 / 4.0 = ', 10.0 / 4.0

# Exponent: performs exponention calculation 2**3 = 2 raised to the power of 3 
print '2**3 = ', 2**3

# Floor: Floor division is division where the result of the division is rounded down to the nearest integer
print '11.//3.=', 11.//3.

# Note: you can do few arithmetic operations on strings (addition and multiplication) in python! 
# The only arithmetic you will need to do in this course is addition; see the example below:
print 'hello, ' + 'world!'

# There is a shorthand for arithmetic when assigning the result to a variable
# For example, x += 2 is equivalent to x = x + 2
x = 4
print 'x = ', x
x += 2
print 'x += 2 = ', x
