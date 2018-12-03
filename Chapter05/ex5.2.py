# Sandeep Sadarangani 3/12/18
# Fermats Theorem check

def check_fermat(a,b,c,n):
    
    result = 0
    
    calc = a**n + b**n
    calc_test = c**n
    
    if(calc == calc_test):
        result = 1
    
    return result
    

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
n = int(input("Enter value for n: "))

result = check_fermat(a,b,c,n)

if(result == 1):
    print("Fermat was wrong!")
else:
    print("No, that doesn't work")
