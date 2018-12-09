# Sandeep Sadarangani 7/12/18
# Mutability of Lists


# FUNCTION - Generate a list with elements 0 to n-1
def generate_list(l, n):
	for i in range(n):
		l.append(i)


# Generate new list
x = []
generate_list(x, 10)
print(x)


# Edit a list - Mutable
x[0] = 5
print(x)
	

# FUNCTION - Test if an element is in a list
def element_test(l, elem):
	if test in x:
		print("The element {} is in the list".format(test))
	else:
		print("The element {} is NOT in the list".format(test))


# Using the 'in' operator to test if an element is in the list

test = 7
element_test(x, test)

test = 19
element_test(x,test)
