# Sandeep Sadarangani 4/12/18
# Factorial with check

def factorial(n):
    if not isinstance(n, int):  # isinstance() is an in-built function which checks if a value is of a specific type
    
        print("Factorial only defined for integers")
        return None
    elif n < 0:
        print("Can't have negative factorials")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
        
print(factorial(2.4))
