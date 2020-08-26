#!/usr/bin/env python
import numpy
import numpy as np
# Below is a blank canvas to start your assignment
def count_to_n(num) :
    if num > 0 :
        count_to_n(num - 1)
        print num, ' '

#count_to_n(1)
#count_to_n(2)
#count_to_n(3)

def count_to_n_for(num) :
    print "For loop"
    for x in range(2, num+1):
        print x

def count_to_n_to(num) : 
    print "While loop"
    x = 2
    while x <= num:
        print x
        x += 1

#count_to_n_for(10)
#count_to_n_to(10)

def count_to_10() : 
    for x in range(1, 11):
        if x % 2 == 0 :
            print float(x)
        else : 
            print x

#count_to_10()

def Sum_Division() :
    sum = 0
    x = 0
    while x < 200 :
        if x % 2 == 0 and x % 7 == 0 :
            sum += x
        x += 1
    print sum

#Sum_Division()

#print "Part 1B"
#intarray3 = [0, 1, 2, 3]
#intarray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#two_n = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9] 
#print two_n[7]
#count = 0
#for x in range(0,10) : 
#    if two_n[x]% 8 == 0 :
#        count += 1

#print count


#matrix = [[3,4], [5,6]]
#print matrix[1]
#print matrix[0]

print "Part C"
#two_n = numpy.array([2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9])
#print len(two_n)
#three_n = numpy.array([3**0, 3**1, 3**2, 3**3, 3**4, 3**5, 3**6, 3**7, 3**8, 3**9])
#result = three_n - two_n
#print result

array_1 = numpy.array([1., 2.])
array_2 = numpy.array([3., 4.])
list_1 = [1., 2.]
list_2 = [3., 4.]

#print array_1 + array_2
#print list_1 + list_2

vector_array = [5.3, 6.2, 9.5]
magni_vector = np.linalg.norm(vector_array)

#print magni_vector
#x = np.array([5.3, 6.2, 9.5])
#print np.linalg.norm(x)

def create_unit_vector(array) :

    magni_vector = np.linalg.norm(array)
    unit_vector = array / magni_vector
    print "Total unit vector", np.linalg.norm(unit_vector)
    return unit_vector

print create_unit_vector(vector_array)
