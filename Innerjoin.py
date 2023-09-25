#!/usr/bin/env python
# coding: utf-8

# In[12]:


file_path = '/Users/hfakhrav/Desktop/Data scientist2023/Join Project/Datasets/ward.p'  # Replace with the actual file path
with open(file_path, 'rb') as file:
    ward = pickle.load(file)


# In[29]:


print(ward.head())


# In[14]:


file_path = '/Users/hfakhrav/Desktop/Data scientist2023/Join Project/Datasets/census.p'  # Replace with the actual file path
with open(file_path, 'rb') as file:
    census = pickle.load(file)


# In[28]:


print(census.head())


# In[17]:


file_path = '/Users/hfakhrav/Desktop/Data scientist2023/Join Project/Datasets/taxi_owners.p'  # Replace with the actual file path
with open(file_path, 'rb') as file:
    taxi_owners = pickle.load(file)


# In[19]:


print(taxi_owners.head())


# In[23]:


file_path = '/Users/hfakhrav/Desktop/Data scientist2023/Join Project/Datasets/taxi_vehicles.p'  # Replace with the actual file path
with open(file_path, 'rb') as file:
    taxi_vehicles = pickle.load(file)


# In[24]:


print(taxi_vehicles.head())


# In[ ]:


## nner join Chicago data portal dataset To help us learn about merging tables, we will use data from the city of Chicago data portal.

##In this example, we want to merge the local government data with census data about the population of each ward.


# In[25]:


import pandas as pd


# In[31]:


ward_census = ward.merge(census, on='zip', suffixes=('_ward','_cen'))


# In[32]:


print(ward_census.head())


# In[ ]:




