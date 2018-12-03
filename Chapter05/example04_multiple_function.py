# Sandeep Sadarangani 3/12/18
# In a function: Given x and y, determine if x is a multiple of y

x = 71
y = 7


def divisible(x, y):
    if(x%y == 0):
        print("x is divisible by y")
    else:
        print("x is NOT divisible by y")
        
        
divisible(x,y)