# Sandeep Sadarangani 4/12/18
# Improved recursive palindrom function

def first(word):
    return word[0]
    
def last(word):
    return word[-1]
    
def middle(word):
    return word[1:-1]
    
    
def palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return palindrome(middle(word))
        
        
print(palindrome("kayak"))