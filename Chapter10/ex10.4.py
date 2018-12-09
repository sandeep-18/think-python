# Sandeep Sadarangani 9/12/18
# Function that modifies the list and returna none

def chop(l):
    del(l[0])
    l.pop()


t = [1,2,3,4]
print(t)
chop(t)
print(t)