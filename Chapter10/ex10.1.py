# Sandeep Sadarangani 9/12/18
# Function that takes a list of lists and adds up the sum

def nested_sum(l):
    sum = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            sum = sum + l[i][j]
    return sum
    
    
test_l = [[1,2], [3], [4,5,6]]
print(nested_sum(test_l))


test_l2 = [[21,32], [1,2,4], [9,7], [3,5,4]] # 88
print(nested_sum(test_l2))


