#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pwd


# In[12]:


pd.read_csv(r"C:/Users/ABC/Desktop/Project/csv/Movie-Ratings.csv")


# In[17]:


df = pd.read_csv(r"C:/Users/ABC/Desktop/Project/csv/Movie-Ratings.csv")


# In[40]:


print(df)


# # Q1)  list of top 10 movie(descending order) in terms of budget

# In[56]:


df.sort_values('Budget (million $)',ascending=False)


# # Q2) list of top 10 movie (ascending order) in terms of budget

# In[57]:


df.sort_values('Budget (million $)',ascending=True)


# # Q3) Which genre is the best in terms of price budget

# In[59]:


df.loc[[304], :]


# In[60]:


df.iloc[[304], [1,4]]


# # Q4)	distribution(graph) of audience rating

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


pd.read_csv(r"C:/Users/ABC/Desktop/Project/csv/Movie-Ratings.csv")


# In[7]:


df = pd.read_csv(r"C:/Users/ABC/Desktop/Project/csv/Movie-Ratings.csv")


# In[8]:


print(df)


# In[9]:


sns.distplot(df['Audience Ratings %'])


# # Q5)	Distribution(graph) of critics rating (rotten tomato)

# In[10]:


sns.distplot(df['Rotten Tomatoes Ratings %'])


# # Q6)	Distribution of budget

# In[13]:


sns.boxplot(y='Budget (million $)',x='Genre',data=df)


# # Q7)	Distribution of critics rating

# In[14]:


sns.boxplot(y='Rotten Tomatoes Ratings %',x='Genre',data=df)


# # Q8)	Distribution of audience rating

# In[15]:


sns.boxplot(y='Audience Ratings %',x='Genre',data=df)


# # Q9)	Histogram of critics rating

# In[14]:


df.hist(column='Rotten Tomatoes Ratings %')


# # Q10)	histogram of audience rating

# In[15]:


df.hist(column='Audience Ratings %')


# # Q11)	Show the total count of all the different genre present in the dataset

# In[32]:


sns.countplot(x='Genre',data=df)


# # Q12)	Show the graph of rating based on genre

# In[39]:


sns.barplot(x='Audience Ratings %',y='Genre',data=df)


# # Q13)	Scatter plot of critics rating vs audience rating

# In[19]:


df.plot.scatter(x='Rotten Tomatoes Ratings %' , y='Audience Ratings %')


# # Q14)	Box plot based on genre and critics rating

# In[17]:


sns.boxplot(x='Genre',y='Rotten Tomatoes Ratings %',data=df)


# # Q15)	Bx plot based on genre and audience rating

# In[18]:


sns.boxplot(x='Genre',y='Audience Ratings %',data=df)


# # Q16)	Pairplot of the whole data set

# In[31]:


sns.pairplot(df)


# # Q 17)	Histogram of  top 10 movie(descending order) in terms of budget

# In[11]:


xyz=df.sort_values('Budget (million $)',ascending=False).head(10)
xyz
plt.hist(xyz['Budget (million $)'])


# # Q18) Histogram of  top 10 movie(ascending order) in terms of budget

# In[12]:


xyz=df.sort_values('Budget (million $)',ascending=True).head(10)
xyz
plt.hist(xyz['Budget (million $)'])


# # Q19)	Joint Plot of critics rating and audience rating (with type as hexagonal)

# In[20]:


sns.jointplot(x='Rotten Tomatoes Ratings %',y='Audience Ratings %',data=df,kind='hex')


# # Q20)	Joint plot of budget vs genre (type as scatter)

# In[23]:


sns.boxplot(x='Budget (million $)',y='Genre',data=df)


# In[ ]:




