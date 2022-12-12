#!/usr/bin/env python
# coding: utf-8

# # Objective

# ## Questions
# 
# - What is the overall sales trend?
# - What are the top 10 products by sales?
# - What are the most selling products?
# 

# # Importing Required Libraries

# In[19]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time


# # Opening the excle Sales data file

# In[20]:


df = pd.read_csv('C:/Users/saura/anaconda3/MySalesAnalysisProject/SalesData/MySalesData.csv')
print(df.head())


# # Printing out Order Date

# In[21]:


print(df['Order Date'])


# # Changing the format using datetime function to get Year

# In[22]:


df['dtime']=pd.to_datetime(df['Order Date'])
    


# In[23]:


df['Year']=df['dtime'].dt.strftime('%Y')


# In[24]:


print(df['Year'])


# # Using tail function to show last 5 records 

# In[25]:


df.tail()


# # Using Grouping and Sum function to get AllSales and Year Total

# In[26]:



df['AllSales']=pd.to_numeric(df['Total Price'], errors='coerce')


df.groupby('Year')['AllSales'].sum()


# # Ploting a graph for the Sales per Year data

# In[50]:


df_trend = df.groupby('Year').sum()['AllSales'].reset_index()
#df = sdata.groupby["AllSales"]

plt.plot(df_trend['Year'],df_trend['AllSales'])
#plt.show()


# # Using Head function to get 5 records

# In[28]:


df.head()


# # Using dataFrame and Sort function to get the top 10 product Sales records

# In[29]:


prod_sales = pd.DataFrame(df.groupby('Product').sum()['AllSales'])

prod_sales.sort_values('AllSales',ascending=False)

#Top 10 product
prod_sales[:10].sort_values('AllSales',ascending=False)




# # From data taking out top 10 most Ordered Product using sort_values and decending order functions

# In[30]:


most_sell_prod = pd.DataFrame(df.groupby('Product').sum()['Quantity Ordered'])


# In[31]:


top_10_products=most_sell_prod.sort_values('Quantity Ordered',ascending=False)

top_10_products[:10]


# # Calculating "Total Cost" by using multiplier function per line item

# In[32]:



df['TotalCost']=df['Quantity Ordered']*df['Cost']

df.head()


# # Calculating "Profit" by using subtract function per line item

# In[33]:


df['Profit']=df['Total Price']-df['TotalCost']
df.head()


# # Top 10 Most Profitable products

# In[45]:


Total_Profit = pd.DataFrame(df.groupby('Product').sum()['Profit']) 

Total_Profit=Total_Profit.sort_values('Profit',ascending=False)

Total_Profit[:10]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




