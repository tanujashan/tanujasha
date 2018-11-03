import matplotlib.pyplot as plt
# x-coordinates of left sides of bar 

left=[2,4,6,8,10]

#heights of bar
height=[10,20,30,40,50]

#labels of bar 
tick_label=['one','two','three','four','five']

#ploting a bar chart 
plt.bar(left,height,tick_label=tick_label,width=0.5,color=['purple','blue'])

#naming the x-axis
plt.xlabel('x-axis')

#naming the y-axis
plt.ylabel('y-axis')

#plot title
plt.title('bar graph') 

#function to plot a graph
plt.show()