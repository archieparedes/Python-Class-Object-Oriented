"""
CSC 243 Python for Programmers Assignment 5
Created on Nov Thu 09 13:39:27 2017
@author: Archie Paredes
Problem 8.37
"""
import math
class Square:
    def __init__(self, squareBase):
        self.sB = squareBase
    # Returns Calculated permimeter for perfect square
    def perimeter(self):
        return(4 * self.sB)
    # Returns Calculated area for perfect square
    def area(self):
        return(self.sB * self.sB)

class Triangle:
    def __init__(self, triangleBase):
        self.tB = triangleBase
    # Returns Calculated permimeter for equilateral triangle
    def perimeter(self):
        return(3 * self.tB)
    # Returns Calculated area for equilateral triangle
    def area(self):
        return((self.tB**2) * (math.sqrt(3)) / 4)

# Example:
sBase = int(input("Please Enter the base of your perfect square: "))
s = Square(sBase)
print("Perimeter:",s.perimeter())
print("Area:", s.area())

tBase = int(input("Please Enter the base of your equilateral triangle: "))
t = Triangle(tBase)
print("Perimeter:",t.perimeter())
print("Area:", t.area())
    
