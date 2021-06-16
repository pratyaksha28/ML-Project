# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 02:05:31 2021

@author: DELL
"""
####Preprocessing to extract sales for all the products of the first store only
import pandas as pd
import numpy as np
df = pd.read_csv("train.csv")
df['date']=pd.to_datetime(df['date'])
df['dayofweek'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

data = []
k = 0
data.append(df['dayofweek'][0:18260].tolist())
data.append(df['month'][0:18260].tolist())
data.append(df['year'][0:18260].tolist())
arr = np.array(df['sales'], dtype='float')
for i in range(50):
    temp = arr[k:18260+k] 
    data.append(temp) 
    k = k+18260

data = np.array(data)
data = data.T

pd.DataFrame(data).to_csv("sales.csv",index=False)

