#!/usr/bin/env python

# There are two ways to build a list

# 1. Put in everything at the start
# Remember: A matrix is just a list of lists (freshmanGrades)

fallGrades = [85, 93, 76, 92, 95, 89]
springGrades = [90, 91, 84, 88, 87, 95]
freshmanGrades = [fallGrades, springGrades]

# 2. Build it incrimentally by using the append method

student_ID = []
print 'initial student ID', student_ID
student_ID.append('Bevo')
student_ID.append(18)
student_ID.append('freshman')
student_ID.append('bevo40')
student_ID.append(3.4)
print 'final student ID', student_ID

# You can check the length of a list with len

NumberClasses = len(fallGrades)
print 'ID Length: ', len(student_ID)


# And there are a few ways to get information out of them

# 1. Indexing (Note: Starts at zero!)

first_grade = fallGrades[0]
second_grade = fallGrades[1]
last_grade = fallGrades[- 1]
print 'fallGrades[0] = ', first_grade
print 'fallGrades[1] = ', second_grade
print 'fallGrades[length - 1] = ', last_grade

# 2. Iterating over the list with a for loop

for grade in fallGrades:
	print 'Grade: ', grade

# 3. Just printing it out
print 'Student ID: ', student_ID
print 'Freshman Grades: ', freshmanGrades

# Lastly you can use indexing in lists of lists or matrices

matrix = [[0,1],[2,3]]

print 'matrix:',matrix
print 'matrix[0][1]:',matrix[0][1] # print the values from the 1st list (0) and the 2nd value in that list 
