# Sandeep Sadarangani 3/12/18
# Area of a circle function

import math

def area(radius):
    area_of_circle = math.pi * (radius ** 2)
    return area_of_circle
    
    
    
radius = 5
a1 = area(radius)
print("Circle has area: " + str(a1) + "units square")