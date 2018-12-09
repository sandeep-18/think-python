# Sandeep Sadarangani 9/12/18
# Takes a list and checks if any elemnents appear more than once

def has_duplicates(l):
    for i in range(len(l)-1):
        for z in range(len(l)-1-i):
            if l[i+1+z] == l[i]:
                return True
    return False
    

def has_duplicates2(l):
    for i in range(len(l)-1):
        if l[i] in l[i+1:]:
            return True
    return False
        
    
    
word =("hellpl")
print(has_duplicates2(word))

word = "ohimzke"
print(has_duplicates2(word))