#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df = pd.read_csv (r'D:\Python\Programs\Import CSV to SQL\ADJUSTMENTLIST.csv')
df1 = pd.read_csv (r'D:\Python\Programs\Import CSV to SQL\ADJUSTMENTLIST_Test.csv')

#Data Comparision
def DataComparision():
    df_numOfRows = df.shape[0]
    print('Number of Rows in Source file : ', df_numOfRows)
    df1_numOfRows = df1.shape[0]
    print('Number of Rows in Target file : ', df1_numOfRows)
    Count = df_numOfRows-df1_numOfRows

    if Count == 0:
        print("There is no difference in the source and target file\n")
    else:
        print(f'There is {Count} record difference in both file')
        #Test_MissingOrNaNValues()
    print("-------------------------------------------------------------------------------")
DataComparision()

#Merge two csv files by inner
df3 = pd.merge(df, df1, 
                   on='Account', 
                   how='inner')
df3


# In[16]:


#Merge two csv files by left
df3 = pd.merge(df, df1, 
                   on='Account', 
                   how='outer')
df3


# In[ ]:




