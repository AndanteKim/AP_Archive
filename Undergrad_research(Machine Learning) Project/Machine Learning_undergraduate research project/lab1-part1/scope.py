#!/usr/bin/env python

#################################################################
# Scope is a term used to describe where a variable can be used #
# If you try to use a variable before you have declared it, the #
# computer doesn't know what you're talking about		#
#################################################################

# This line causes an error because the computer doesn't know what
# temperature is yet. Move this line so it doesn't cause an error

temperature = 75

print temperature



# There is scope within functions. If you declare a variable in a
# function, once you leave the function the variable is lost

def foo(num):
    fooNum = num + 1
    print 'Inside the function'
    print 'fooNum = ', fooNum
    return fooNum

# The lines below should produce an error 
# Edit both the function, foo, and the lines below so that you can 
# extract fooNum from the function foo 
fooNum = foo(13)
print 'Outside the function'
print 'fooNum = ', fooNum

# You can print variables defined outside of a function within 
# a function as shown below 

a = 2
def print_a():
    print 'The value of a is',a

print_a()
# you can also use a variable in an arithmetic expression

def print_a_times_2():
    print 'The value of a*2 is',a*2

print_a_times_2()

# However, if you try to change the value of a variable defined
# outside a function (a) within a function (add_one), python will produce an error

# Below I will walk you through two ways to fix this issue: 

# First, add a new first line within the function add_one with "global a"; this will allow 
# you to edit variable a within the function

# Second, create a new function called add_one_new that takes a variable, x, and 
# returns x + 1.  When calling the function use a as the input variable and reset 
# the value of variable a as the output of the function.  I would suggest using the second solution.
# For example, a = dummy_function(a)

a = 10
def add_one(a):
    a = a + 1
    return a
print add_one(a)

# Lastly, see what happens if you define a variable with in a function that has also been 
# declared outside of the function 

x = 5 
def declare_x():
    x = 2 
    print 'The value of x inside the function =', x

declare_x()
print 'The value of x outside the function =', x


