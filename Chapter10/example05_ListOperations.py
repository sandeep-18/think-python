# Sandeep Sadarangani 7/12/18
# Using List Operations - + and *

# FUNCTION - Concatenate two lists
def add_lists(l1, l2):
	new_list = l1 + l2
	return new_list
	
	
# FUNCTION repeat a list n number of times
def repeat_list(l, n):
	new_list = l * n
	return new_list
	


# TESTING

def testing():

	print("Creating new list...")
	x = [384, 39, 30, 12]
	y = ["hello", "how", "are", "you"]
	print("Lists are: x = {}, y = {}".format(x,y))
	
	print("\nConcatenating Lists")
	new_l = add_lists(x,y)
	print("New list = {}".format(new_l))
	
	
	
	print("Multiplying List")
	new_l = repeat_list(x, 4)
	print("New list = {}".format(new_l))
	
	
	
testing()
