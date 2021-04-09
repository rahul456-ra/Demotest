#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_csv (r'D:\Python\Programs\Import CSV to SQL\ADJUSTMENTLIST.csv')
df1=df.groupby('Area')
for Area, Area_df in df1:
         print(Area)
         print(Area_df)


# In[5]:


df1.get_group('SW')


# In[ ]:




