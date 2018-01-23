from die import Die

import pygal

die1 = Die()

die2 = Die(10)

results = []

for roll_num in range(1000):
	result = die1.roll() + die2.roll()
	results.append(result)
	
frequencies = []
max_result = die1.num_sides + die2.num_sides

'''
for value in range(2,max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)
'''
	
frequencies = [results.count(value) for value in \
range(2,max_result + 1)]
	
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
#hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12',\
#'13','14','15','16']
hist.x_labels = [str(x) for x in range(20,max_result + 21)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10',frequencies)
hist.render_to_file('dice10_visual.svg')
