import unittest
from city_fit import city_function

class CityTestCase(unittest.TestCase):
	'''Test city_fit.py'''
	def test_city_fit_function(self):
		city_name = city_function('santigo','chile')
		self.assertEqual(city_name,'Santigo,Chile')
	
	def test_city_population_function(self):
		city_name = city_function('santigo','chile',10000)
		self.assertEqual(city_name,'Santigo,Chile - population 10000')
	
unittest.main()
