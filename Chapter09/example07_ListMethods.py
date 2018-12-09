# Sandeep Sadarangani 7/12/18
# List Methods - append, extend, sort
# These are internal methods of the lists which change the lists and return None


# FUNCTION - Append an item to a list
def append_list(l, elem):
	l.append(elem) # This will add the element to the end of the list
	

# FUNCTION - extend a list by adding another list (concatenation)
def extend_list(l1,l2):
	l1.extend(l2)
	
	
# FUNCTION - sort a list (alphabetically or numerically)
def sort_list(l):
	l.sort()



# TESTING
def testing():
	x = [25,28,92,99,72]
	y = [23,84,92,92]
	new_element = 78
	print("List 1 = {}, List 2 = {}, new_element = {}".format(x,y,new_element))
	
	
	print("\nTesting Append with List 1 and new_element")
	append_list(x,new_element)
	print(x)
	
	
	print("\nExtending List 1 with List 2")
	extend_list(x,y)
	print(x)
	
	print("\nSorting List1")
	sort_list(x)
	print(x)
	
	
	
testing()
