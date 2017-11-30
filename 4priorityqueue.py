"""
CSC 243 Python for Programmers Assignment 5
Created on Nov Thu 09 10:00:34 2017
@author: Archie Paredes
Problem 8.36
"""
# class that adds to list, looks at min, checks if list is empty, return length, and remove min
class PriorityQueue:
    def __init__(self, initial = []):
        self.s = initial
    # Add integer
    def insert(self,inputval):
        self.s.append(inputval) 
    # Returns Minimum Number
    def min(self):
        return(min(self.s))
    # If the list is empty, this will return True, else false
    def isEmpty(self):
        if (len(self.s) == 0): return True
        else: return False
    # This will remove the min from initial s list
    def removeMin(self):
        self.s.remove(min(self.s))
    # Returns List
    def __len__(self):
        return(len(self.s))
    
    
    
    


    
        
        
    
        


