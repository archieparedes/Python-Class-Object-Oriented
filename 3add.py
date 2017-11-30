"""
CSC 243 Python for Programmers Assignment 5
Created on Nov Thu 09 06:29:27 2017
@author: Archie Paredes
Problem 8.34
"""
# Class that looks at list, mean, return length ,and also clears list
class Stat(list):
    def __init__(self, initial = []):
        self.s = initial
    def add(self, inputval):
        self.s.append(inputval) 
    # Use of Python built in fuctions for max, min, sum
    def max(self):
        return(max(self.s))
    def min(self):
        return(min(self.s))
    def sum(self):
        return(sum(self.s))
    def mean(self):
        return(sum(self.s)/len(self.s))
    # Emptying list
    def clear(self):
        self.s = []
    # Length
    def __len__(self):
        return(len(self.s))
    
    
    
    


    
        
        
    
        


