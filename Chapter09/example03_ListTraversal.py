# Sandeep Sadarangani 7/12/18
# Traverse a list using for and while loop

#FUNCTION - List traversal using for loop
def for_traverse(l):
	for i in l:
		print(i)
		
		
# FUNCTION - List Traversal using while loop
def while_traverse(l):
	index = 0
	while index < len(l):
		print(l[index])
		index = index + 1
		

# FUNCTION - List creation
def list_creation(l,n):
	for i in range(n):
		l.append(i)

		
# TESTING FUNCTION
def testing():
	
	print("Creating List...")
	x = []
	list_creation(x, 10)
	print("Created List: x = {}".format(x))
	
	
	print("\nTesting Traversal using for loop...\n")
	for_traverse(x)
	
	print("\nTesting Traversal using while loop...\n")
	while_traverse(x)
	
	print("End of Testing")
	
	
	
# Main
testing()
