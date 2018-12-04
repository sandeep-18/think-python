# Sandeep Sadarangani 4/12/18
# Converging function

def sequence(n):
    while n!= 1:
        print(n, end = " ")
        if n%2 == 0:
            n = n//2
        else:
            n = n*3 + 1
    print("")
            

sequence(3)