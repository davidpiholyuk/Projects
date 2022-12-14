# -*- coding: utf-8 -*-
"""Data_Analysis_David_Piholyuk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/davidpiholyuk/e03f779ce77e6d4b216e37045d1e69aa/data_analysis_david_piholyuk.ipynb
"""

#David Piholyuk
#03/21/2021

#This program reads in data from kc_house_data.csv (obtained from https://www.kaggle.com/harlfoxem/housesalesprediction)
'''This program provides the following data visualizations: scatter plot of sq. footage vs house price, 
bar chart of average price based on how many bathrooms the house has, and a box plot of house prices
'''
#This program will provide answer for the following questions:
#What is the average housing costs in King County?

#Does the number of bathrooms affect the cost of the house?

#Does more square footage mean more money?


#import libraries
import matplotlib.pyplot as plt
import seaborn as sb

#define function
#(Sorry I know this is really simple but I really couldn't think of another function to call)

def flt(item):
  item = float(item)
  return item

#Main program

#read the data into a list

with open('kc_house_data1.csv', 'r') as house:
  data = house.readlines()

data.pop(0)

#verify that the data was read in correctly
#print(data)

#data cleaning

price = []
bathroom = []
sqfeet = []
for i in data:
  id, date, prices, bedrooms, bathrooms, sqft_living, sqft_lot,floors, waterfront, view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, sqft_living15, sqft_lot15 = i.split(',')
  prices = flt(prices)
  bathrooms = flt(bathrooms)
  sqft_living = flt(sqft_living)

  price.append(prices)
  bathroom.append(bathrooms)
  sqfeet.append(sqft_living)

#Create data visualizations and analysis

#scatter plot of house prices vs sq. footage
sq_graph = sb.scatterplot(x = sqfeet , y = price)
sq_graph.set_title('Square Footage vs. House Prices ')
sq_graph.set(xlabel = 'Sq. Feet', ylabel = 'House Prices in Milliona (USD)')

plt.show()

print('Each of these points represent a house which has been sold between 2014 and 2015 in the King County.')
print('Looking at this scatter plot we can see that there is evidently a relationship between square footage and house prices.')
print('The variable on the y-axis represents the amount the house sold for in millions, for example 1 would mean the house sold for one million USD')
print('The variable on the x-axis represents the amount of square footage of living space the house has.')
print('It is evident that there is a positive association between square footage and the house prices. This means typically as square footage rises so does the house prices')
print('There appears to be 4-6 outliers in the data.')
print('')

#Bar chart for bathrooms vs. house price
br_graph = sb.scatterplot(x = bathroom, y = price)
br_graph.set_title('Number of Bathrooms vs. House Prices ')
br_graph.set(xlabel = 'Bathrooms', ylabel = 'House Prices in Millions (USD)')

plt.show()

print('Each of these points represent a house which was sold between 2014-2015 in the King County. This graph shows the relationship between bathrooms and house price.')
print('Looking at this scatter plot we can see that there is evidently a relationship between square footage and house prices.')
print('The variable on the y-axis represents the amount the house sold for in millions.')
print('The variable on the x-axis represents the amount of bathrooms the house has.')
print('It appears that there is a slight positive association between numbers of bathrooms and the house prices. This means that the more bathrooms the house has the more likely it is to have a higher house price.')
print('There appears to be 4-6 outliers in the data.')
print('')


#create a box plot of the house prices to rule out if there are any outliers
box_graph = sb.boxplot(price)
box_graph.set_title('House Prices ')

plt.show()

print('This box chart confirms that there are multiple outliers in the data as some of the houses sold for way more than the others.')

#Answering questions 
print('')
print('')
print('')

#1.
print('#1. What is the average cost of house prices in King County, WA?')

#I had to calculate this manually with excel because I kept getting a float object is not iterable error
print(f'The average house price in King County is $540,063.15')

print('')
#2.
print('#2. Does the number of bathrooms affect the cost of the house?')

print('After looking at the data we can conclude that it is not always the case that the house costs more if it has more bathrooms')
print('but, the data does show that there is a higher chance of the house being worth more if there are more bathrooms.')

#3.

print('')
print('#3. Does more square footage mean more money?')

print('Yes, the data shows that there is a clear correlation between square footage and house prices. The scatter plot seems to have a linear relationship between the house price and the amount of square feet of living space.')