import unittest

class Employee():
	
	def __init__(self,first_name,last_name,salary = 0):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary
		self.name = self.first_name +' ' + self.last_name
		self.name = self.name.title()
		
	def give_raise(self,raises=5000):
		if raises == '':
			mesg = self.name + "'s raising salary is : "+ str(5000)
			return mesg
		else:
			mesg = self.name + "'s raising salary is : "\
			+ str(self.salary + raises)
			return mesg
			
#emp = Employee('Jan','Li')
#print(emp.give_raise())

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.myEmployee = Employee('Jan','Li')
		self.raise_salary = 1000
		
	def test_give_default_raise(self):
		mesg = self.myEmployee.give_raise()
		self.assertEqual(mesg,"Jan Li's raising salary is : 5000")
		
	def test_give_custom_raise(self):
		mesg = self.myEmployee.give_raise(self.raise_salary)
		self.assertEqual(mesg,"Jan Li's raising salary is : 1000")
		
unittest.main()
