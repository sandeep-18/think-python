# Sandeep Sadarangani 3/12/18
# Slicing in python - Strings


#Slicing is from [n:m] which includes n but DOES NOT include m

s = "Monty Python"
print(s[0:5])

print(s[6:12])


word = "Hellohowareyou" # To get word 'how' we need from 5->8
print(word[5:8])


# OTHER TIPS

# Omitting the first part of the indexing starts from the beginning i.e. [:m]
print(word[:5])

# Similiarly [n:] prints til the end
print(word[8:])

# [:] gives the whole word
print(word[:])
