# Sandeep Sadarangani 3/12/18
# A function that determines whether a number is even or odd

def isEven(num1):
    status = 0
    if num1%2 == 0:
        status = 1
    return status
    
    
x = 2

if(isEven(x)):
    print("Number is even")
else:
    print("Number is odd")