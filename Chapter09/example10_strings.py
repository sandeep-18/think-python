# Sandeep Sadarangani 7/12/18
# Converting a string to list elements using - list()
# Converting a list to a string using - .join()
# Breaking a string using a delimiter using - .split(delimiter)


# FUNCTION - string_to_list: take a string and convert it to a list
def string_to_list(word):
	print("The string is: {}".format(word))
	new_list = list(word)
	print("The list is: {}".format(new_list))
	

# FUNCTION - break_string: Break a string by a delimiter into a list
def break_string(word):
	print("The string is: {}".format(word))
	new_list = word.split(" ")
	print("The list is: {}".format(new_list))
	
# FUNCTION - join_list: Join a list of strings into a complete string
def join_list(l):
	print("The list is: {}".format(l))
	delimiter = " "
	new_string = delimiter.join(l)
	print("The string is: {}".format(new_string))

# Testing
def testing():
	
	word = "Hello"
	
	string_to_list(word)
	
	
	sentence = "Hello how are you going ?"
	break_string(sentence) # Creates a list of strings
	
	l1 = ["hello", "good", "to", "see", "you"]
	

testing()
