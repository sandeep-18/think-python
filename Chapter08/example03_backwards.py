# Sandeep Sadarangani 3/12/18
# A function that takes a string as an argument and displays the letters backwards
# one per line

def backwards(word):
	i = len(word) - 1
	while i >= 0:
		print(word[i])
		i = i -1
		
backwards("Hello")
