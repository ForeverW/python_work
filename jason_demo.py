import json

numbers = [1,2,3,4,5,6,10,-10]

try:
	fname = "E:\\C_GCC\\python_work\\data_source\\number.json"
	with open(fname,'w') as f_obj:
		json.dump(numbers,f_obj)
except FileNotFoundError:
	print("No such file")
else:
	print('Json data save sucess')


print('Load json data')

try: 
	with open(fname) as f_robj:
		number_read = json.load(f_robj)
except FileNotFoundError:
	print('No such file')
else:
	print(number_read)
	
