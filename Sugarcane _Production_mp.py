#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns 
from matplotlib import pyplot as plt


# In[2]:


df = pd.read_csv("List of Countries by Sugarcane Production.csv")


# In[3]:


df.head()


# In[4]:


df.shape #col and rows 


# # Data Cleaning

# In[7]:


df["Production (Tons)"] = df["Production (Tons)"].str.replace(".","")
df["Production per Person (Kg)"] = df["Production per Person (Kg)"].str.replace(".","").str.replace(",",".")
df["Acreage (Hectare)"] = df["Acreage (Hectare)"].str.replace(".","")
df["Yield (Kg / Hectare)"]= df["Yield (Kg / Hectare)"].str.replace(".","").str.replace(",",".")


# In[8]:


df.head(10)


# In[9]:


df = df.drop( "Unnamed: 0", axis = 1)


# In[10]:


df.rename(columns= {"Production (Tons)": "Production(Tons)"}, inplace = True)
df.rename(columns= {"Production per Person (Kg)": "Production_per_person(Kg)"}, inplace = True)
df.rename(columns= {"Acreage (Hectare)": "Acreage(Hectare)"}, inplace = True)
df.rename(columns= {"Yield (Kg / Hectare)": "Yield(Kg/Hectare)"}, inplace = True)


# In[11]:


df.head()


# In[12]:


df.isna().sum()


# In[13]:


df[df["Acreage(Hectare)"].isnull()]


# In[14]:


df = df.dropna().reset_index().drop("index", axis = 1)


# In[15]:


df


# In[16]:


df.nunique()


# In[17]:


df.dtypes


# In[18]:


df["Production(Tons)"] = df["Production(Tons)"].astype(float)
df["Production_per_person(Kg)"] = df["Production_per_person(Kg)"].astype(float)
df["Acreage(Hectare)"] = df["Acreage(Hectare)"].astype(float)
df["Yield(Kg/Hectare)"] = df["Yield(Kg/Hectare)"].astype(float)


# In[19]:


df.dtypes


# # Univariate Analysis

# In[20]:


df.head(7)


# In[21]:


df["Continent"].value_counts()


# In[22]:


df["Continent"].value_counts().plot(kind = "bar")


# In[23]:


df.describe()


# # Checking Outliers

# In[25]:


plt.figure(figsize=(12,10))

plt.subplot(2,2,1)
sns.boxplot(df["Production(Tons)"])
plt.title("Production(Tons)")

plt.subplot(2,2,2)
sns.boxplot(df["Production_per_person(Kg)"])
plt.title("Production_per_person(Kg)")

plt.subplot(2,2,3)
sns.boxplot(df["Acreage(Hectare)"])
plt.title("Acreage(Hectare)")

plt.subplot(2,2,4)
sns.boxplot(df["Yield(Kg/Hectare)"])
plt.title("Yield(Kg/Hectare)")

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.4, wspace=0.4)

plt.show()


# In[26]:


plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
sns.distplot(df["Production(Tons)"])
plt.title("Production(Tons)")
plt.subplot(2,2,2)
sns.distplot(df["Production_per_person(Kg)"])
plt.title("Production_per_person(Kg)")
plt.subplot(2,2,3)
sns.distplot(df["Acreage(Hectare)"])
plt.title("Acreage(Hectare)")
plt.subplot(2,2,4)
sns.distplot(df["Yield(Kg/Hectare)"])
plt.title("Yield(Kg/Hectare)")
plt.show()


# In[28]:


sns.violinplot(y=df["Production(Tons)"])


# # Bivariate Analysis 

# In[29]:


df.head(7)


# ### Let's check the country which produces maximum sugarcane???

# In[30]:


df_new = df[["Country","Production(Tons)"]].set_index("Country")


# In[31]:


df_new


# In[32]:


df_new["Production(Tons)_percent"] = df_new["Production(Tons)"]*100/df_new["Production(Tons)"].sum()


# In[33]:


df_new


# In[37]:


# Horizontal bar chart
df_new["Production(Tons)_percent"].plot(kind='barh', figsize=(10,6))
plt.title("Production(Tons) Percent Distribution")
plt.xlabel("Percentage")
plt.show()


# In[38]:


#pie chart 
df_new["Production(Tons)_percent"].plot(kind = "pie", autopct = "%.2f")
#Brazil, India and China have 65% of production of sugarcane 


# In[39]:


#vertical bar chart
df_new["Production(Tons)_percent"].plot(kind='bar', figsize=(10,6))
plt.title("Production(Tons) Percent Distribution")
plt.ylabel("Percentage")
plt.show()


# In[40]:


df[["Country","Production(Tons)"]].set_index("Country").sort_values("Production(Tons)", ascending = False).head(15).plot(kind = "bar")


# In[41]:


ax = sns.barplot(data = df.head(15),  x= "Country", y = "Production(Tons)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# # Country which has highest land 

# In[45]:


df_acr = df.sort_values("Acreage(Hectare)", ascending= False).head(15)
ax = sns.barplot(data = df_acr,  x= "Country", y = "Acreage(Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# # Which country has highest yield per hectare?
# 

# In[47]:


df_yield = df.sort_values("Yield(Kg/Hectare)", ascending = False).head(15)
ax = sns.barplot(data = df_yield,  x= "Country", y = "Yield(Kg/Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# # Which country has highest production?

# In[48]:


df_yield = df.sort_values("Production_per_person(Kg)", ascending = False).head(15)
ax = sns.barplot(data = df_yield,  x= "Country", y = "Production_per_person(Kg)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()


# ## Correlation

# In[49]:


df.corr()


# In[53]:


sns.heatmap(df.corr(), annot=True, cmap="Blues")
plt.show()


# # Do countries with highest land produce more sugarcane?

# In[54]:


sns.scatterplot(data = df, x = "Acreage(Hectare)", y = "Production(Tons)", hue = "Continent" )


# Overall increase in land increases the production

# # Do countries which yield more sugarcane per hectare produces more sugarcane in total?
# 

# In[55]:


sns.scatterplot(data = df, x = "Yield(Kg/Hectare)" , y = "Production(Tons)", hue = "Continent")


# In[56]:


df.head()


# # Analysis for Continent

# In[57]:


df_continent = df.groupby("Continent").sum()


# In[58]:


df_continent["number_of_countries"] = df.groupby("Continent").count()["Country"]


# In[59]:


df_continent


# # Which continent produces maximum sugarcane?

# In[60]:


df_continent["Production(Tons)"].sort_values(ascending=False).plot(kind="bar", color="green")
plt.title("Production(Tons) by Continent")
plt.ylabel("Production(Tons)")
plt.show()


# # Do number of countries in a Continent effects production of sugarcane?

# In[61]:


continent_names = df_continent.index.to_list()
sns.lineplot(data = df_continent,x = "number_of_countries", y= "Production(Tons)" )
plt.xticks(df_continent["number_of_countries"], continent_names, rotation =90)
plt.show()


# # Do continent with highest land produces more sugarcane?
# 

# In[62]:


sns.lineplot(data = df_continent,x = "Acreage(Hectare)", y= "Production(Tons)" )


# # Production distribution by continent

# In[63]:


df_continent["Production(Tons)"].plot(kind = "pie", autopct = "%.2f%%")
plt.title('Production Distribution by Continent')
plt.show()


# # Correlation for continent

# In[64]:


df_continent.corr()


# In[ ]:




