#!/usr/bin/env python

# A variable is something that can store a value, and this value can be changed
# In Python, any variable can hold any type of value. It's important that you give
# your variables descriptive names, otherwise you won't know what the variable represents later.
# Below are examples of different kinds of values, called types, you can store in variables.

# Integer: an integer, can be positive or negative
year = 2017

# Float: a number with a decimal point, can be positive or negative
gpa = 3.0

# Boolean: either true or false, can also be represented as 1 and 0.
isStudent = True

# String: any amount of text, always needs to be in quotations.
slogan = 'Hook em!'

# The value of variables can change

print 'gpa before variable change'
print gpa
gpa = 3.4 # This line overrides the old value of gpa and replaces it, called reassignment
print 'gpa after variable change'
print gpa

# You can print the type of variable using the "type" 
print 'gpa is a',type(gpa)

# Note you can also print multiple variables by seperating them with a comma 
