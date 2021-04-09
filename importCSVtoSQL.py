#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import pyodbc as pdobc
#Import CSV file from folder path
data = pd.read_csv (r'D:\Python\Programs\Import CSV to SQL\ADJUSTMENTLIST.csv')
df2 = pd.DataFrame(data, columns= ["Account Label","Account","Account Type","Adjustment Description","Area"])

#Rename columns
df2.rename(columns={'Account Label': 'AccountLabel', 'Account': 'AccountNumber','Account Type': 'AccountType','Adjustment Description': 'AdjustmentDescription'}, inplace=True)


# Connect to SQL Server
conn = pdobc.connect('Driver={SQL Server};'
                      'Server=RAHULMOG;'
                      'Database=PythonPractice;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table in Database
cursor.execute('''
               IF OBJECT_ID('ADJUSTMENTLIST', 'U') IS NOT NULL
               DROP TABLE ADJUSTMENTLIST 
               CREATE TABLE ADJUSTMENTLIST ([Account Label] [varchar](100) NULL,
                                                    [Account Number] [varchar](100) NULL,
                                                    [Account Type] [varchar](100) NULL,
                                                    [Adjustment Description] [varchar](100) NULL,
                                                    [Area] [varchar](100) NULL
                                                    )
              ''')


# Insert File Data to SQL Table
for row in df2.itertuples():
    cursor.execute('''
                INSERT INTO PythonPractice.dbo.ADJUSTMENTLIST([Account Label],
                                                    [Account Number] ,
                                                    [Account Type] ,
                                                    [Adjustment Description] ,
                                                    [Area])
                VALUES (?,?,?,?,?)
                ''',
                row.AccountLabel, 
                row.AccountNumber,
                row.AccountType,
                row.AdjustmentDescription,
                row.Area
                )
conn.commit()


# In[ ]:





# In[ ]:




