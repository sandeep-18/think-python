# Sandeep Sadarangani 4/12/18
# Exercise 6.2 - Write the Ackermann function A(m,n)

def ackermann(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    elif m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))
    else:
        return None
        
print(ackermann(3,4))



# Stack Diagram
# ackerman(3,4)
#       -> A(2, A(3,3))
#       -> A(2, A())