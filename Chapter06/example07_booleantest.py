# Sandeep Sadarangani 3/12/18
# Divisibility function using booleans

def is_divisible(x, y):
    if x%y == 0:
        return True
    else:
        return False
        
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

if(is_divisible(x,y)):
    print("x is divisible by y")
else:
    print("x is NOT divisible by y")
