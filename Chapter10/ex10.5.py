# Sandeep Sadarangani 9/12/18
# Function that checks if list is sorted in ascending order

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
            
    return True
    
    
l1 = [1,2,3]
print(is_sorted(l1))

l2 = [3,1,4,34,5]
print(is_sorted(l2))

l3 = ['a', 'b', 'd', 'c']
print(is_sorted(l3))