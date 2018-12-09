# Sandeep Sadarangani 7/12/18
# Creating new list objects

x = [1,2,3,4]  # x is an identifier which points to the the first element of the list

print(x)
print("Type of list is: {}".format(type(x))


# FUNCTION: Print a list element-wise
def print_list(l):
  for i in l:
    print(i)


print_list(x)

# Creating a list of strings
words = ["Hello", "how", "are", "you"]
print_list(words)

# Creating a list of mixed types
random = ["Hello", 4, 7.12, True]
print_list(random)


# Creating a nested list
nested_list = ["Next", words, "six", x]
print_list(nested_list)
