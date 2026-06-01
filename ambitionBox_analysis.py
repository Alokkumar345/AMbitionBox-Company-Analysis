#!/usr/bin/env python
# coding: utf-8

# # ambitionBox analysis

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns


# In[ ]:


print("hello")


# # 1. Data Loading

# In[ ]:


df=pd.read_csv("companies.csv")
df


# In[ ]:


df.head() # data show


# In[ ]:


df.tail()


# In[ ]:


df.columns


# In[ ]:


df.shape


# # 2. Data Understanding (EDA Start)

# In[ ]:


df.info()


# In[ ]:


df.describe()


# In[ ]:


# data type
df.dtypes


# In[ ]:


df.nunique()


# # 3. Missing Values Analysis

# In[ ]:


df.isnull().sum()


# In[ ]:


df[df.isnull().any(axis=1)]
# df[df['location'].isnull()]


# In[ ]:


df['location'] = df['location'].fillna('Unknown')


# In[ ]:


# (3.4k) remove () and convert 3.4k
df['reviews'] = df['reviews'].str.replace(r'[()]', '', regex=True)


# In[ ]:


df.dtypes


# In[ ]:


df.head()


# In[ ]:


# convert 1.2 L into 120000
def convert_reviews(x):
    x = x.strip('()')
    if 'L' in x:
        return float(x.replace('L', '')) * 100000
    elif 'k' in x:
        return float(x.replace('k', '')) * 1000
    else:
        return int(x)

df['reviews'] = df['reviews'].apply(convert_reviews)



# In[ ]:


# convert data type
df['reviews']=df['reviews'].astype('int64')


# # 4. Duplicate Analysis

# In[ ]:


df.duplicated().sum()


# In[ ]:


# show duplicate
df[df.duplicated()]


# In[ ]:


df[df['name']=="Wheelseye Technology"]


# In[ ]:


df=df.drop_duplicates()


# In[ ]:


df.shape


# # 5. data cleaning

# In[ ]:


df['name'] = df['name'].str.strip()


# In[ ]:


df['name']


# In[ ]:


# outliers
import matplotlib.pyplot as plt

df.boxplot(column='rating')
plt.show()


# In[ ]:


# top rated comapney
df.sort_values('rating', ascending=False).head(10)


# In[ ]:


# low rated comapney
df.sort_values('rating').head(10)


# In[ ]:


# avg rating by location
df.groupby('location')['rating'].mean().sort_values(ascending=False)


# In[ ]:


# avg rating by industry
df.groupby('industry')['rating'].mean().sort_values(ascending=False)


# 

# In[ ]:


df = df[(df['rating'] >= 1) & (df['rating'] <= 5)]


# In[ ]:


import matplotlib.pyplot as plt

df['rating'].hist(bins=10)
plt.show()


# In[ ]:


top10 = df.sort_values('reviews', ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(top10['company_name'], top10['reviews'])
plt.xticks(rotation=90)
plt.title("Top 10 Companies by Reviews")
plt.show()


# In[ ]:


df


# In[ ]:


# rename columns
df=df.rename(columns={
    'name':"company_name"
})


# In[ ]:


location_rating = df.groupby('location')['rating'].mean().sort_values(ascending=False).head(10)

location_rating.plot(kind='bar')
plt.title("Average Rating by Location")
plt.show()


# In[ ]:


plt.figure(figsize=(8,5))

plt.scatter(df['reviews'], df['rating'], alpha=0.6)

plt.xlabel("Number of Reviews")
plt.ylabel("Rating")
plt.title("Relationship Between Reviews and Rating")

plt.show()


# In[ ]:


plt.scatter(df.index, df['reviews'], color='red', label='Reviews')
plt.scatter(df.index, df['rating'], color='green', label='Rating')

plt.legend()
plt.show()


# In[ ]:


plt.boxplot(df['rating'])
plt.title("Rating Boxplot")
plt.show()


# In[ ]:


df.groupby('company_name')['rating'].max().sort_values(ascending=False).head(5)


# In[ ]:


def rating_category(rating):
    if rating >= 4.0:
        return "Excellent"
    elif rating >= 3.0:
        return "Good"
    else:
        return "Bad"

df['rating_category'] = df['rating'].apply(rating_category)


# In[ ]:


df


# # END project

# In[ ]:




