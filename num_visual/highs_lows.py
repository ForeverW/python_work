import csv
from datetime import datetime

from matplotlib import pyplot as plt

#filename = 'sitka_weather_07-2014.csv'
#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'	

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs, lows = [], [], []
	
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
			
		#highs.append(row[1])
		
	#print(highs)
	
fig = plt.figure(dpi = 128,figsize = (10,6))
#plt.plot(highs, c = 'red')
plt.plot(dates,highs,c = 'red')
plt.plot(dates,lows,c = 'blue')

plt.fill_between(dates,highs,lows,facecolor = 'blue', alpha = 0.1)

title = "Daily high and low temperature - 2014\nDeath Valley,CA"
plt.title(title,fontsize=24)

#plt.title("Daily high temperatures, 2014",fontsize = 24)
plt.xlabel('',fontsize = 16)

fig.autofmt_xdate()

plt.ylabel("Temperature(F)",fontsize = 16)
plt.tick_params(axis = 'both', which = 'major',labelsize = 16)

plt.show()
	
'''
	for index, column_header in enumerate(header_row):
		print(index,column_header)
'''

