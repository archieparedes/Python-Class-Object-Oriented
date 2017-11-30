"""
CSC 243 Python for Programmers Assignment 5
Created on Nov Tue 07 15:58:37 2017
@author: Archie Paredes
Problem 8.22
"""
class Worker:
    def __init__(self, nameInput = '', hourInput = 0):
        self.name = nameInput
        self.hour = hourInput
        
    def pay(self,rateInput):
        return('Not implemented')

class SalariedWorker:
    # Assuming 580 is the stock rate
    def __init__(self, nameInput = '', hourInput = 0):
        self.name = nameInput
        self.hour = hourInput
    def pay(self, rateInput):
        return(580.0)
    
class HourlyWorker:
    def __init__(self, nameInput = '', hourInput = 0):
        self.name = nameInput
        self.hour = hourInput
    
    def changedRate(self, newrate):
        self.rate = newrate
        
    def pay(self, rateInput):
        return(rateInput * self.hour)

        
    
    


    

