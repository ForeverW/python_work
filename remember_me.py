import json
import os

username = input("What's your name? ")

file_name = 'E:\\C_GCC\\python_work\\data_source\\username.json'

try:
	with open(file_name,'w') as f_obj:
		json.dump(username,f_obj)
		print("We'll remember you when you come back,"+
		username + "!")
except FileNotFoundError:
	print('Not found such file')

#os.chdir("E:\\C_GCC\\python_work")

print(os.getcwd())

f_rname = "E:\\C_GCC\\python_work\\data_source\\username.json"

try:
	with open(f_rname) as fr_obj:
		u_name = json.load(fr_obj)
except FileNotFoundError:
	print('Not found' +  f_rname)
	with open(f_rname,'a') as fr_obj:
		u_name = input("Input your Name: ")
		json.dump(u_name,fr_obj)
		print("We'll remember you")
else:
	print("Hello,"+ u_name+" welcome back")
