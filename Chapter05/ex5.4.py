# Sandeep Sadarangani 3/12/18
# Analyse the recursive function


def recurse(n,s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        
        
recurse(3,0)

#recurse(3,0)
#	recurse(2, 3)
#		recurse(1, 5)		
#			recurse(0, 6)
#				print 3