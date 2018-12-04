# Sandeep Sadarangani 4/12/18
# Palindrome - Recursively determine if a word is a palindrome

def first(word):
    return word[0]
    
def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:  # If word is odd length or even (1 or 0 characters) then it is palindrome
        return True
    else:
        if(first(word) == last(word)): # Check first and last word are equal
            return True and is_palindrome(middle(word))
        else:
            return False
        
            
word = "Racecar"
            
print(is_palindrome(word.upper()))