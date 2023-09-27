
import math 

class Circle:
    pass

def create(radius):
    c=Circle()
    c.radius=radius
    return c

def perimeter(circle):
    return 2 * math.pi * circle.radius

