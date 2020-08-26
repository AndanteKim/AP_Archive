#!/usr/bin/env python

#########################################################################
# Functions are blocks of code that can be executed by calling their name.
# They're useful when you have something you want to reuse and not rewrite.
# Python gives you lots of built in functions, but you can build your own.
#########################################################################

# To define a function, say def and then name your function. This is the function
# heading. End the heading with the colon, and after this is the function body,
# which will be executed when 
def printGreeting():
	print 'Hello! Welcome to the introduction to functions script.'


# You have the option of including parameters, which are variables that are given
# values when the function is called. Include in the parentheses of the heading.
def printCustomGreeting(name):
	print 'Hello, ' + name + '! Welcome to the introduction to functions script.'


# You also have the option of returning a value, which can be saved or used.
def volume(length, width, height):
	volume = length * width * height
	return volume

# Lastly, your function can return as many variables as you like
def returnxyz(x,y,z):
    return x,y,z


# To use a function, just call it by saying it's name, including parameters if needed
printGreeting()
printCustomGreeting('Bevo')
volume333 = volume(3, 3, 3)
print 'What is the volume of a 3 x 3 x 3 box? ', volume333
# You can call a function as many times as you would like with various variables as input
print 'What is the volume of a 4 x 1 x 5 box? ', volume(4, 1, 5)
a,b,c = returnxyz(1,2,3)
print 'a=',a,' b=',b, ' c=',c

