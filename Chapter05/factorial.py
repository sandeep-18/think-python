# Sandeep Sadarangani 3/12/18
# Recursive factorial function

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
        
        
print(factorial(19))
