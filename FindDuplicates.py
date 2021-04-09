#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
data = pd.read_csv (r'D:\Python\Programs\Import CSV to SQL\ADJUSTMENTLIST.csv')
def duplicaterecord():
    duplicate_Records=data[data.duplicated()]
    print(f'Duplicate records in Source file are: \n {duplicate_Records}')
duplicaterecord()






    


# In[ ]:





# In[ ]:




