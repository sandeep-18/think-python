# Sandeep Sadarangani 3/12/18
# Distance function

import math


def distance(x1,y1,x2,y2):
    dy = y2-y1
    dx = x2-x1
    result = math.sqrt(dx**2 + dy**2)
    return result
    
    

d = distance(1,2,4,6)
print(d)