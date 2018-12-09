# Sandeep Sadarangani 9/12/18
# Cumulative sum of list

def cumsum(l):
    new_l = []
    sum = 0
    for i in l:
        sum = sum + i
        new_l.append(sum)
    
    return new_l
    
    
test_l = [1,2,3]
print(cumsum(test_l))

test_l_2 = [1,556,34,546,322,23]
print(cumsum(test_l_2))