#!/usr/bin/env python

#########################################################################################
## Below are examples of control flow statements.
## Try to figure out what this script will print before running it. 
#########################################################################################

isStudent = True
isFreshman = False
isSophomore = True
isJunior = False
isSenior = False
isGraduated = False
year = 2
classList = ['BioStats', 'OChem', 'FRI', 'VAPA', '408D']

# IF STATEMENTS: If the condition is true, the body will be executed
# Here, 'isStudent' is the condition, and everything indented after the colon is the body

print 'If Statement Example:'
if isStudent:
    print 'Welcome to class'
if isGraduated:
    print 'Welcome to adulthood'


# IF/ELSE STATEMENTS: If the condition is false, execute the else body

print
print 'If/Else Statement Example'
if isGraduated:
    print 'Welcome to adulthood'
else:
    print 'Not a graduate yet! Go to class.'


# ELIF STATEMENTS: A chain of If/Else statements can be used, with 'elif' in the middle.
# This is just shorthand for "Else if", and will only be evaluated if the previous 
# condition is false. Once one statement body has been executed, no more are evaluated.

print
print 'Elif Statement Example'
if isFreshman:
   print 'Welcome to UT!'
elif isSophomore:
   print 'Welcome back!'
elif isJunior: 
   print 'Almost there!'
elif isSenior:
   print 'Do NOT get senioritis!'
else:
   print 'She doesn\'t even go here'


