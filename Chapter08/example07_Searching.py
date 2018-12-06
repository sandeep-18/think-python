# Sandeep Sadarangani 5/12/18
# A function that finds a letter in a word using a while loop

def find(word, letter, start):
    index = start
    while index < len(word):
        if letter == word[index]:
            return index
        index = index + 1
    return -1
        
        
index_found_at = find("How are you", 'o',2)
print(index_found_at)
