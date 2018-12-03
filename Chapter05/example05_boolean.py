# Sandeep Sadarangani 3/12/18
# A function that takes in two numbers and determines if they are equal

def equality(num1, num2):
    isEqual = 0
    if num1 == num2:
        isEqual = 1
    
    return isEqual
    
x = 7
y = 7

equality_check = equality(x, y)

if equality_check:
    print("Numbers are equal")
else:
    print("Numbers are not equal")
        
