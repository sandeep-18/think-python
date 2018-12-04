# Sandeep Sadarangani 4/12/18
# Learnig to index strings

fruit = 'banana'
colour = 'apple'

# Start indexing at element 0
print(fruit[2]) # n
print(colour[4]) # e

# len() is an in built function that returns the # of characters in a string
print(len(fruit))
print(len(colour))

# A shortcut to get the last letter of a string
print(fruit[len(fruit)-1]) # a
print(colour[len(colour)-1]) # e

# If we try to access an element that is not part of the string
# We will get IndexError: string index out of range\

#print(colour[len(colour)])  # Gives us an index error

# We can also get the last letter using negative indexing
print(fruit[-1])


def last_letter_test(word):
	if word[len(word)-1] != word[-1]:
		return False
	return True

print(last_letter_test("Hello"))
