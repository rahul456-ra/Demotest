#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RAHULMOG;'
                      'Database=PythonPractice;'
                      'Trusted_Connection=yes;')

sql_query = pd.read_sql_query(''' 
                              select * from PythonPractice.dbo.ADJUSTMENTLIST
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2

df = pd.DataFrame(sql_query)
df
df.to_csv (r'D:\Python\Programs\Import CSV to SQL\export_data.csv', index = False)


# In[ ]:




