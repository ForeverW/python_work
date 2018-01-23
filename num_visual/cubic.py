import matplotlib.pyplot as plt

plt.figure(1)

x_values = [1,2,3,4,5]
y_values = [1,8,27,64,125]

plt.plot(x_values,y_values,c='red',linewidth = 2)

plt.title('Cubic data',fontsize = 15)
plt.xlabel('x_values',fontsize = 14)
plt.ylabel('value of cubic',fontsize =14)

plt.tick_params(axis = 'both', labelsize = 14)

plt.savefig('cubic_line.png',bbox_inches = 'tight')

plt.figure(2)
plt.scatter(x_values,y_values,c = y_values,cmap = plt.cm.Blues,
edgecolor = 'none',s =40)

plt.savefig('cubic_scatter.png',bbox_inches = 'tight')

plt.show()
