# Sandeep Sadarangani 3/12/18
# A function that recursively prints strings

def print_n(s, n):
    if n <= 0:
        print("End of string repetition")
        return
    else:
        print(s)
        print_n(s, n-1)
        

print_n("Hello", 5)