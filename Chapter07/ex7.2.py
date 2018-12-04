# Sandeep Sadarangani 3/12/18
# Create an eval function: takes in string and evaluates it

import math

def eval_loop():
    
    while True:
        word = input('Enter Command: ')
        if word == 'done':
            break
        else:
            print(eval(word))
        
            
            
eval_loop()