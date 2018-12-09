# Sandeep Sadarangani 9/12/18
# Function that takes a list and returns all elems minus outer elems

def middle(l):
    new_l = l[1:len(l)-1]
    return new_l
    
    
t = [1,2,3,4]
print(middle(t))

t = [34,434,2343,23,23,2343,23443,345,73,34]
print(middle(t))