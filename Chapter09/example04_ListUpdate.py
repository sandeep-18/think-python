# Sandeep Sadarangani 7/12/18
# Updating a list using list traversal
# When writing/updating elements in a list, use a combination of range() and len()

# FUNCTION:Using for - Multiply every element in a list by 2
def multiply_by_two(l):
	for i in range(len(l)):
		l[i] = l[i] * 2
		

# FUNCTION:Using while - Multiply every element in a list by 2
def multiply_by_two_while(l):
	index = 0
	while index < len(l):
		l[index] = l[index]*2




		
		
# TESTING

def testing():

	print("Creating List")
	x = [23,45,23,57,45,476,34]
	y = list(x) # NOTE: if y=x then y is pointing to the same list. Need to use list() to create a new instance of list
	print("List is: x = {}".format(x))
	
	
	print("\nMultiplying Every Element by 2")
	multiply_by_two(x)
	print("List is: x = {}".format(x))
	
	
	print("\nMultiplying Every Element by 2 - While Loop")
	multiply_by_two(y)
	print("List is: x = {}".format(y))
	

# Main

testing()
		
