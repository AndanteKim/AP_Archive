#!/usr/bin/env python
import math
# Below is a blank canvas to start your assignment
#print "Part 1B"

#my_age = 25

#if my_age == 25:
#   print True
#else: print False
#print bool(my_age==25)
#def compute_kinetic_energy(mass, velocity):
#    kinetic_energy = 0.5 * mass * math.pow(velocity,2)
#    return kinetic_energy

#Former = compute_kinetic_energy(5, 10)
#Latter = compute_kinetic_energy(3, 11)
#if Former < Latter :
#    print Former, 'and', Latter
#    print "The former is less than the latter."
#elif Former == Latter :
#    print Former, "and", Latter
#    print "Both are equal."
#else :
#    print Former, "and", Latter
#    print "The former is more than the latter."

#def greater_than_5_and_even(x) :
#    return bool(x > 5 and x % 2 == 0)

#print greater_than_5_and_even(3)
#print greater_than_5_and_even(4)
#print greater_than_5_and_even(6)
#print greater_than_5_and_even(7)

#print "Part 1C"

#def even_or_odd(x):
#    if x % 2 == 0 :
#        sentence = "even"
#        return sentence
#    else :
#        sentence = "odd"
#        return sentence

#print even_or_odd(10)
#print even_or_odd(11)

#def is_sidec_5(a, b):
#    c = math.sqrt(math.pow(a,2) + math.pow(b,2))
#    if c < 5 :
#        result = "side c is less than 5."
        
#    elif c == 5 :
#        result = "side c is equal to 5."
#       
#    else :
#        result = "side c is greater than 5."
#    return result

#print is_sidec_5(3,4)
#print is_sidec_5(1,2)
#print is_sidec_5(4,6)

def morse_potential_energy(r, re, De):
    a = 5
    potential_energy = De * math.pow(1 - math.pow(math.e, -a * (r - re)),2)
    return potential_energy

def status_of_bond(r):
    re = 1
    De = 1
    energy = morse_potential_energy(r,re,De)
    if r > re and energy > 0 and energy < 1 :
        result = "The bond is stretched."
    elif r > re and energy == 1 or energy == 0 :
        result = "The bond is broken."
    else :
        result = "The condition does not match." 
    return result

#print morse_potential_energy(0.5,1,1)
#print morse_potential_energy(1.0,1,1)
#print morse_potential_energy(1.5,1,1)
#print morse_potential_energy(6.0,1,1)

print status_of_bond(0.5)
print status_of_bond(1.0)
print status_of_bond(1.5)
print status_of_bond(6.0)
