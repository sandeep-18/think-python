# Sandeep Sadarangani 03/12/18
# Testing a recursive function

def countdown(n):
    if n <= 0:
        print("Blastoff")
    else:
        print(n)
        countdown(n-1)
        
        
countdown(25)