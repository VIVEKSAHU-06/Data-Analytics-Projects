"""CUSTOMER LIFETIME VALUE ANALYSIS"""
## Customer lifetime value analysis is used to estimate the total value of a customer to the business over the lifetime of their relationship.

## By analyzing customer lifetime values , companies can identify the most effective marketing channels and campaigns for aquiring high value customers. To make and develop targeted retention strategies to keep those customers engaged and loyal.

"""Process of customer lifetime value"""
# 1. Customer aquisition cost.
# 2. Marketing budget.
# 3. Return on Investment (ROI).
# 4. Long term profit
# 5. Customer retension cost.
# 6. Indivisual customer profit.
# 7. Customer valueation.

"""Objectives"""
# 1. Make a visualization for the distribution of customer aquisition cost. 
# 2. Create a visualization for the revenue generated by the customer.
# 3. Commpare the cost of aquisition across various channels and determines which once are the most and least profitable.
# 4. Find out which channels are the most and least effective at converting customers.
# 5. Calculate the total revenue of the channel and analyze the most and least profitable channels in terms of generating revenue.
# 6. Calculate the return on investment (ROI) for each channel.

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as pg
import plotly.colors as pc

data = pd.read_csv('data/customer_acquisition_data.csv')
# print(data)

"""Make a visualization for the distribution of customer aquisition cost"""
# fig = px.histogram(data,
#                 x='cost',
#                 nbins=20,
#                 title="Distribution of customer aquisition cost"  )
# fig.show()

"""Create a visualization for the revenue generated by the customer"""
# fig = px.histogram(data,
#                 x='revenue',
#                 nbins=20,
#                 title="Distribution of revenue"  )
# fig.show()

"""Commpare the cost of aquisition across various channels and determines which once are the most and least profitable"""
# profitable_chanel = data.groupby('channel')['cost'].mean().reset_index()
# print(profitable_chanel)
# fig = px.bar(profitable_chanel,
#              x='channel',
#              y='cost',
#              title="Cost of aquisition across various channels")
# fig.show()

"""Find out which channels are the most and least effective at converting customers"""
# highest_conversion_chanel = data.groupby('channel')['conversion_rate'].mean().reset_index()
# print(highest_conversion_chanel)
# fig = px.bar(highest_conversion_chanel,
#              x='channel',
#              y='conversion_rate',
#              title="Most and least effective channels")
# fig.show()

"""Calculate the total revenue of the channel and analyze the most and least profitable channels in terms of generating revenue"""
# revenue_by_channel = data.groupby('channel')['revenue'].sum().reset_index()
# print(revenue_by_channel)
# fig = px.pie(revenue_by_channel,
#              names='channel',
#              values='revenue',
#              hole=0.5 ,
#              title="Revenue by different channels")
# fig.show()

"""Calculate the return on investment (ROI) for each channel"""
data['roi'] = data['revenue']/data['cost']

roi_by_channel = data.groupby('channel')['roi'].mean().reset_index()
fig = px.bar(roi_by_channel,
             x='channel',
             y='roi',
             title="Return on Investment")
fig.show()
# print(data.columns)