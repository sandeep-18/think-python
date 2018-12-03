# Sandeep Sadarangani 3/12/18
# Calculate the area of a circle given centre and point on perimeter
import math
    
def area_rad(radius):
    return math.pi * (radius**2)
    
def distance(x1,y1,x2,y2):
    dy = y2-y1
    dx = x2-x2
    return math.sqrt(dx**2 + dy**2)    

def area_of_circle(xc, yc, xp, yp):
    radius = distance(xc,yc,xp,yp)
    return area_rad(radius)


area = area_of_circle(1,3,5,6)
print("The area of the circle is " + str(area) + " units squared")