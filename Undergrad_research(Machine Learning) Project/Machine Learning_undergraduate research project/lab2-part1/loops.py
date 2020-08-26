#!/usr/bin/env python

#########################################################################################
## Below are examples of for and while loops.
## Try to figure out what this script will print before running it. 
#########################################################################################


# WHILE LOOPS: While a condition is true, execute the body

print
print 'While Loops Example:'
year = 1
while year <= 4:
    print 'Welcome to class, round ' + str(year)
    year += 1


# FOR LOOPS: For an conditional number of iterations, execute the body. 
# Here, the loop is executed 5 times. 'loopNumber' will store how many iterations we have done.
# If this is a new variable with no previous value, it starts at 0
# The condition also be done as range(variable). For other options, look at the documentation

print
print 'For Loops Example:'
for loopNumber in range(5):
    print loopNumber

# You can also stop the loop, or break the loop, under certain conditions

print 
print 'Example of breaking from a loop' 
for loopNumber in range(5):
    print loopNumber
    if loopNumber > 2:
        break


