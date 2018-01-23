import json

import pygal

from countries import get_country_code

from pygal.style import RotateStyle,LightColorizedStyle

#add date to a list
filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)

cc_populations = {}
#print the population of each country in 2010
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population
			
			#print(code + ":" + str(population))
		#else:
			#print('Error - ' + country_name)
		#print(country_name + ":" + str(population))
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}

for cc,pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

vm_style = RotateStyle('#336699',base_style = LightColorizedStyle)
		
vm = pygal.maps.world.World(style = vm_style)
vm.title = 'World Population in 2010, by Contry'
vm.add('0 - 10m',cc_pops_1)
vm.add('10m - 1 bn',cc_pops_2)
vm.add('>1bn',cc_pops_3)

vm.render_to_file('world_population.svg')
