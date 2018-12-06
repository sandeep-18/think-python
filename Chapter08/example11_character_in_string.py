# Sandeep Sadarangani 5/12/18
# A function which will list all the similar characters between 2 strings

def similar(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


similar("Hello", "telleor")