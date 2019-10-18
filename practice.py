# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 01:16:56 2019

@author: mytufail
"""

import pandas as pd
ri=pd.read_csv('ri_withdatetime.csv',parse_dates=True, index_col='stop_datetime')


"Ex. 1"

#Calculating the hourly arrest rate
#When a police officer stops a driver, a small percentage of those stops ends in an arrest.
# This is known as the arrest rate. In this exercise, you'll find out whether the 
# arrest rate varies by time of day.
#
#First, you'll calculate the arrest rate across all stops. Then, you'll 
#calculate the hourly arrest rate by using the hour attribute of the index. 
#The hour ranges from 0 to 23, in which:
#
#0 = midnight
#12 = noon
#23 = 11 PM
#Instructions
#100 XP
#Take the mean of the is_arrested column to calculate the overall arrest rate.
#Group by the hour attribute of the DataFrame index to calculate the hourly arrest rate.


# Calculate the overall arrest rate
print(ri.is_arrested.mean())

# Calculate the hourly arrest rate
print(ri.groupby(ri.index.hour).is_arrested.mean())

# Save the hourly arrest rate
hourly_arrest_rate = ri.groupby(ri.index.hour).is_arrested.mean()
#%%

"Ex. 2"


#Plotting the hourly arrest rate
#In this exercise, you'll create a line plot from the hourly_arrest_rate object. 
#A line plot is appropriate in this case because you're showing how a quantity 
#changes over time.
#
#This plot should help you to spot some trends that may not have been obvious when 
#examining the raw numbers!
#
#Instructions
#100 XP
#Import matplotlib.pyplot using the alias plt.
#Create a line plot of hourly_arrest_rate using the .plot() method.
#Label the x-axis as 'Hour', label the y-axis as 'Arrest Rate', and title the plot 
#'Arrest Rate by Time of Day'.
#Display the plot using the .show() function.




# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Create a line plot of 'hourly_arrest_rate'
hourly_arrest_rate.plot()

# Add the xlabel, ylabel, and title
plt.xlabel('Hour')
plt.ylabel('Arrest Rate')
plt.title('Arrest Rate by Time of Day')

# Display the plot
plt.show()


"""Conclusion:Wow! The arrest rate has a significant spike overnight, 
and then dips in the early morning hours."""



