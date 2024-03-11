import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('data.csv')
#df.plot()
#plt.show()







#Specify that you want a scatter plot with the kind argument:
#kind = 'scatter'
#A scatter plot needs an x- and a y-axis.
#In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
#Include the x and y arguments like this:
#x = 'Duration', y = 'Calories'


#df = pd.read_csv('data.csv')
#df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
#plt.show()





#Use the kind argument to specify that you want a histogram:
#kind = 'hist'
#A histogram needs only one column.
#A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
#In the example below we will use the "Duration" column to create the histogram:
# import sys
# import matplotlib
# df = pd.read_csv('data.csv')
# # Create the histogram
# df["Duration"].plot(kind='hist')
# # Save the plot to a file named 'histogram.png'
# plt.savefig('histogram.png')
# # Display the plot interactively
# plt.show()
