# Sandeep Sadarangani 3/12/18
# Recursively sum numbers from 1 to n


def recursive_sum(n):
    if n <= 0:              # Base case
        return 0
    else:
        return n + recursive_sum(n-1)      # Recursive case
        
        
        
print(recursive_sum(9))