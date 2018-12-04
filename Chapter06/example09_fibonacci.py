# Sandeep Sadarangani 4/12/18
# Recursive Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
        
print(fibonacci(1.5))

