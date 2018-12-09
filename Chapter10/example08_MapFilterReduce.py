# Sandeep Sadarangani 7/12/18
# Map, Filter and Reduce

# FUNCTION - add all the numbers in a list - FOR LOOP

def sum_list_for(l1):
	total = 0
	for i in l1:
		total = total + i
	return total


# FUNCTION - add all the numbers in a list - WHILE LOOP

def sum_list_while(l1):
	total = 0
	index = 0
	while index < len(l1):
		total = total + l1[index]
		index = index + 1
	return total

# FUNCTION - capitalise all string items and return a new list
def capitalise_all(l1):
	new_list = []
	for ch in l1:
		new_list.append(ch.upper())
	return new_list

		
# Testing
def testing():
	print("Creating List...")
	x = [874, 745, 95, 288, 43]
	y = list(x)
	print("List is x = {}".format(x))
	
	total = sum_list_for(x)
	print(total)
	
	total = sum_list_while(y)
	print(total)
	
	
	print("\nUsing the sum() function")
	total = sum(x)
	print(total)


	str = ["H", "o", "w", "a", "r", "e", "y", "o", "u"]
	print("New List is str = {}".format(str))
	print(capitalise_all(str))

testing()
















