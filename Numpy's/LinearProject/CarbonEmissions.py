# Author: Kyle Angeles
# File: CarbonEmissions.py
# Date-Written -> June 10 2026
# Description -> This is just simply a small python project with introduced new concepts that I've have been learning for past 2-3 days
# using Numpy framework and matplotlib for visualization graphs and pandas 
# This small project is conducted for a particular dataset that has a linear representation using the equation  y = mx + b meaning the slope is going up straight 
# What I'm thinking for going for is for the carbon emission that spans till 2050 if we keep it up 


# Region Libraries 
import numpy as np
import matplotlib.pyplot as plt
import csv 
import pandas as pd 
# EndRegion Libraries 

# Read from the csv file 
df = pd.read_csv("Numpy's/LinearProject/DataSet/OWID_CB_COAL_CO2.csv")


# Axises / plotting data using x and y values 
plt.plot(df['x'], df['y'])

# labels and etc
plt.xLabel("X Axis YEARS")
plt.ylabel("Y Emissions")
plt.title(" Canada's Carbon Emissions over the years")
plt.show()



# Reads the header from the csv data
print(df.h