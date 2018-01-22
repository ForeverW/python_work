#x = [a for a in range(10,1,-1)]
#print(x)


# test random.shuffle function
'''
import numpy as np
import random

a = [1,2,3,4,5,6,7,8,9,0]
b = [1,4,9,16,25,36,49,64,81,0]
c = list(zip(a,b))

print(c)

random.shuffle(c)

print(c)
'''

#test weights initial using 
#[np.random.randn(x,y) for (x,y) in 
#	(sizes[1:],sizes[:-1])]
'''
import numpy as np

sizes = [2,3,2]

def init_para(sizes):
	weights = [np.random.randn(x,y) for (x,y) in 
	(sizes[1:],sizes[:-1])]
	
	print(type(weights))
	print('The length of the weight is:' +str(len(weights)))
	
	for weight in weights:
		print(weight)
		print('\n')
	
init_para(sizes)
'''

#======
'''
#reshape
x = np.random.randn(5,4)

print('X is : ')
print(x)

print('Reshape')

y = np.reshape(x,(2,10))
print(y)

y_x = [np.reshape(a,(2,2)) for a in x]

print(isinstance(y_x,list))
print(type(y_x))

for i in y_x:
	print(i)
	print('\n')
'''
