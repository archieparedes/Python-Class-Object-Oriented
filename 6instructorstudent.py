"""
CSC 243 Python for Programmers Assignment 5
Created on Nov Thu 09 14:31:23 2017
@author: Archie Paredes
Problem 8.38
"""
# Returns age, major or degree 
import time
class Student:
    def __init__(self, nameInput, yearInput, majorInput):
        self.nameInp = str(nameInput)
        self.year = int(yearInput)
        self.majInp = str(majorInput)
    def age(self):
        currentYear = int(time.strftime('%Y', time.localtime()))
        return(currentYear - self.year)     
    def major(self):
        return(self.majInp)
class Instructor:
    def __init__(self, nameInput, yearInput, degreeInput):
        self.nameInp = str(nameInput)
        self.year = int(yearInput)
        self.degInp = str(degreeInput)
    def age(self):
        currentYear = int(time.strftime('%Y', time.localtime()))
        return(currentYear - self.year)     
    def degree(self):
        return(self.degInp)

# Example:
nameInput = str(input('Enter Student Name: '))
yearInput = int(input('Enter year Student was born: '))
majorInput = str(input('What is the study major of the Student?: '))

s = Student(nameInput, yearInput, majorInput)
print('Age by year calculated: ', s.age())
print('Major of the Student: ', s.major())

nameInput = str(input('Enter Instructor Name: '))
yearInput = int(input('Enter year Instructor was born: '))
degreeInput = str(input('What degree did the Instructor graduate with?: '))

t = Instructor(nameInput, yearInput, majorInput)
print('Age by year calculated: ', t.age())
print('Degree of the Instructor ', t.degree())
