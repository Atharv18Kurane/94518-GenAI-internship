"""Exercise 1: Create a math_utils module with functions for area calculations"""
import math

def area_square(side:float):
    return side*side

def area_circle(radius:float):
    return math.pi*radius*radius

def area_rectangle(length:float,breadth:float):
    return length*breadth

def area_triangle(base:float,height:float):
    return 0.5*base*height