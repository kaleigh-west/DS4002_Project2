#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries used for reading data and plotting figures
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Load the cleaned analysis dataset that was used in the model
df = pd.read_csv("sp500_clean.csv", index_col=[0])

# Preview the first few rows to verify data loaded correctly
df.head()


# In[3]:


# Check dataset dimensions (rows, columns)
df.shape


# In[4]:


# Generate summary statistics for closing price
# Provides count, mean, std, min, quartiles, and max
df["SP500"].describe()


# In[5]:


# Plot histogram showing distribution of closing prices
plt.figure(figsize=(6,4))
plt.hist(df["SP500"], bins=50)

# Label axes and title for interpretation
plt.xlabel("Closing Price")
plt.ylabel("Count")
plt.title("Distribution of SP500 Closing Prices")

plt.tight_layout()

plt.savefig('Closing_prices_hist.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.25
           )

plt.show()


# In[6]:


# Create boxplot to visualize spread and outliers in returns
plt.figure(figsize=(5,4))
plt.boxplot(df["SP500"], vert=False)

plt.xlabel("Daily Closing Price")
plt.title("Boxplot of Daily Closing Price")

plt.tight_layout()

plt.savefig('Closing_price_bxplt.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.25
           )

plt.show()


# In[7]:


# Generate summary statistics for returns
# Provides count, mean, std, min, quartiles, and max
df["Returns"].describe()


# In[8]:


# Plot histogram showing distribution of headline lengths
plt.figure(figsize=(6,4))
plt.hist(df["Returns"], bins=50)

# Label axes and title for interpretation
plt.xlabel("Daily Returns")
plt.ylabel("Count")
plt.title("Distribution of SP500 Daily Returns")

plt.tight_layout()

plt.savefig('Returns_hist.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.25
           )

plt.show()


# In[9]:


# Create boxplot to visualize spread and outliers in closing price
plt.figure(figsize=(5,4))
plt.boxplot(df["Returns"], vert=False)

plt.xlabel("Daily Returns")
plt.title("Boxplot of Daily Returns")

plt.tight_layout()

plt.savefig('Returns_boxplt.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.25
           )
plt.show()


# In[10]:


# Date min and max
df["Date"].describe()

