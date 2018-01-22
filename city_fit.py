def city_function(city,country,population=''):
	if population:
		name = city + ',' + country
		name = name.title()
		name = name + ' - population ' + str(population)
	else:
		name = city + ',' + country
		name = name.title()
	return name
	
#print(city_function('shangHai','chaina',10000))
