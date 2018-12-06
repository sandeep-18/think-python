# Sandeep Sadarangani 5/12/18
# A program which counts the number of times a chosen letter has appeared in a string

def count_n(word, letter):
    word = word.lower()
    count = 0
    index = 0
    while index < len(word):
        if word[index] == letter:
            count = count + 1
        index = index + 1
    return count
    
    
print(count_n("Eandeep", 'e'))