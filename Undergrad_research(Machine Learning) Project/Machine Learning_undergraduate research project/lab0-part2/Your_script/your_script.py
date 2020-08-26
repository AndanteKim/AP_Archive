#!/usr/bin/env python
import math
import numpy
# Below is a blank canvas to start your assignment

# output Part 2A in the terminal
#print 'Part 2A'
#print 'hello my name is Andrew Kim'

#print "Part 2B"
my_name = "Andrew Kim"
my_age = 25
#pi = 3.14
#longhorn_rule = True
#print my_name
#print my_age
#print pi
#print longhorn_rule

#print type(my_name)
#print type(my_age)
#print type(pi)
#print type(longhorn_rule)

pi = 3.14159
#print pi
PI = math.pi

#print "Part 2C"
#my_age += 9
#print "My age in 2028 is", my_age
#my_age -=18
#print "My age in 2010 is", my_age

#first = (1+2) * (3+4)
#print first
#second = (7+3)**2 * (2+3)
#print second
#third = (2.0/3.0)*(4.0/5.0)
#print third

#pizzaArea = 12**2 * PI
#print pizzaArea
#pizzaArea = 144*pi
#print pizzaArea

#sentence = "My name is", my_name, "."
#print(sentence)
#print type(sentence)
#print "My name is", my_name,"\b."
#my_age = 25
#remainder = my_age % 2
#print remainder

#KE = 0.5 * 5 * 2**2
#PE = 9.8 * 5 * 5
#print KE + PE

#Part 2D
#print "Part 2D"
#print "The difference of integer and float is", my_age, "and", float(my_age)
#print math.sqrt(36)
#print "e^3 =", math.e**3, "and","e^(-2) =", math.e**-2
#KE = 0.5 * 10 * math.pow(5,2)
#PE = 0.5 * 1000
#total_energy = KE + PE
#print "Total energy of an object is", total_energy

#Part 2E
def print_hello():
    print "'Hello!'"
def print_age(my_age):
    print 'I am', my_age, 'years old'
def compute_kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * math.pow(velocity,2)
    return kinetic_energy
def energy(mass, velocity, height):
    ke1 = 0.5 * mass * math.pow(velocity, 2)
    pe1 = 9.8 * mass * height
    te1 = ke1 + pe1
    return ke1, pe1, te1
print "Part 2E"
print_hello()
print_age(my_age)

mass = 10
velocity = 10
print compute_kinetic_energy(mass, velocity)

mass = 5
velocity = 3
height = 10
ke1,pe1,te1 = energy(mass, velocity, height)
print "Kinetic Energy :", ke1, "Potential Energy :", pe1, "Total Energy :", te1
