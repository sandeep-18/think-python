# Sandeep Sadarangani 4/12/18
# Numerial Approximation of 1/pi
import math

def estimate_pi():
    k = 0
    result = (2*math.sqrt(2))/9801
    summation = 0
    while True:
        
        top = factorial(4*k) * (1103 + 26390*k)
        bottom = (factorial(k)**4) * (396**(4*k))
        fn =  top/bottom
        
        summation = summation + result * fn
        
        if abs(fn) < 1e-15:
            return 1/summation
            
        k = k + 1
        

def factorial(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result
    
    
print(estimate_pi())
