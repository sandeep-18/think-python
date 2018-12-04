# Sandeep Sadarangani 4/12/18
# Exercise 6.1 - Explain the stack for the following program

def b(z):          #b(9)
    prod = a(z,z)  # a(9,9) so prod = 90
    print(z,prod)  # prints: 9, 90
    return prod    # return 90
    
def a(x,y):    # a(9,9)
    x = x + 1   # x = 10
    return x*y  # return 10*9 = 90

def c(x,y,z):       
    total = x + y + z       #total = 9
    square = b(total)**2    # b(9)**2 --> 90^2
    return square    # returns 8100
    
x = 1
y = x + 1
print(c(x, y+3, x+y))   # c(1, 5, 3)


# How the stack is called

# main
#   -> c(1,5,3)
#           -> b(9)
#               -> a(9,9)

