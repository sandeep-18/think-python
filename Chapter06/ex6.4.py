# Sandeep Sadarangani 4/12/18
# A function which determines if a is a power of b

def is_power(a,b):
    if a%b != 0:
        return False
    elif a == b:
        return True
    else:
        return is_power(a//b, b)
        
        
print(is_power(18,3))