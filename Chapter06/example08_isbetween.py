# Sandeep Sadarangani 3/12/18
# A function which determines if the condition is true: x < y < z

def is_between(x, y, z):
    if y >= x and y <= z:
        return True
    else:
        return False
        

print(is_between(1,3,3))