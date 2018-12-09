# Sandeep Sadarangani 9/12/18
# Check if word is an anagram of another word

def is_anagram(word1, word2):
    l1 = list(word1)
    l2 = list(word2)
    
    if len(l1) != len(l2):
        return False
    
    for i in l1:
        if i not in l2:
            return False
    return True
            
            
w1 = "why"
w2 = "hyw"

print(is_anagram(w1,w2))