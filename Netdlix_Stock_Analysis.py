"""NETFLIX STOCK ANALYSIS"""

"""Objectives"""
# 1. Volume stock traded
# 2. Stock price - Open , High , Low , Close.
# 3. Stock price - Day , Month , Yearwise.
# 4. Top 5 dates with highest stock price
# 5. Top 5 dates with lowest stock price

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

from datetime import datetime  

data =pd.read_csv("data/NFLX.csv")
# print(data)
# print(data.head())

sb.set(rc={'figure.figsize':(10,5)})
data['Date'] = pd.to_datetime(data['Date'])
data2 = data.set_index('Date')
# print(data2)

"""Volume of stock price of year on year basis"""
# sb.lineplot(x = data2.index , y = data2['Volume'],label='Volume')
# plt.title("Volume of stock price of year on year basis")
# plt.show()

"""Stock price - Open , High , Low , Close."""
# data2.plot(y=['High','Close','Open'], title="Stock price - Open , High , Low , Close")
# plt.show()

"""Stock price - Day , Month , Yearwise"""
# fig,(ax1,ax2,ax3) = plt.subplots(3, figsize=(15,10))
# data2.groupby(data2.index.day).mean().plot(y='Volume',color = "red",ax = ax1,xlabel = "Day")
# data2.groupby(data2.index.month).mean().plot(y='Volume',color = "blue",ax = ax2,xlabel = "Month")
# data2.groupby(data2.index.year).mean().plot(y='Volume',color = "green",ax = ax3,xlabel = "Year")
# plt.show()

"""Top 5 dates with highest stock price"""
highest_price = data2.sort_values(by='High',ascending=False).head()
# print(highest_price['High'])

"""Top 5 dates with highest stock price"""
lowest_price = data2.sort_values(by='Low',ascending=True).head()
# print(lowest_price['High'])

fig,axes = plt.subplots(nrows=1 , ncols=2, sharex=True, figsize = (12,5))
fig.suptitle("High and Low of stock per period of time",fontsize= 18)
sb.lineplot(ax= axes[0], y = data2['High'],x=data2.index,color='green')
sb.lineplot(ax= axes[1], y = data2['Low'],x=data2.index,color='red')
plt.show()
