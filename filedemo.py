from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
'''
with open("E://C_GCC//python_work//data_source//filedemo.txt") as f:
	for line in f.readlines():
		print('Strip Print')
		print(line.strip())
		#print(len(line.strip())
		
		print('---NoneStrip---')
		print(line)
		#print(len(line))
	print('End')
'''
