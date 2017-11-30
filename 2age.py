"""
CSC 243 Python for Programmers Assignment 5
Created on Nov Thu 09 07:38:59 2017
@author: Archie Paredes
Problem 8.24
"""
# This class will return age or name of person

import time
class Person:
    def __init__(self, nameInput, yearInput):
        self.nameInp = str(nameInput)
        self.year = int(yearInput)
    def age(self):
        currentYear = int(time.strftime('%Y', time.localtime()))
        return(currentYear - self.year)     
    def name(self):
        return(self.nameInp)
