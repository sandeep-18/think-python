# Sandeep Sadarangani 7/12/18
# Multiple ways of deleting elements in a list

x = [5,45,36,7,89,45]
y = list(x)
z = list(x)

print(x is y)


# Method number 1: x.pop([index])
print("List is x = {}".format(x))
print("Command: pop()")
t = x.pop()
print("Pop will capture the value you remove: t = {}".format(t))
print("List is now x = {}".format(x))

print("Command: pop(2)")
t = x.pop(2)
print("Pop will capture the value you remove: t = {}".format(t))
print("List is now x = {}\n".format(x))


# Method number 2: del(y[elem])
print("List is y = {}".format(y))
print("Command: del(y[1])")
del(y[1])
print("List is now y = {}\n".format(y))


# Method number 3: a.remove(element)
print("List is z = {}".format(z))
print("Command: z.remove(89)")
z.remove(89)
print("List is now z = {}".format(z))
 
