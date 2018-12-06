# Sandeep Sadarangani 5/12/18
# Showing that strings are immutable

greeting = "Hello world!"
print(greeting)

# The following line of code is illegal since strings are immutable
# greeting[0] = 'J'
# print(greeting)

# We can create a new variable modifying the current string
new_greeting = 'J' + greeting[1:]
print(new_greeting)