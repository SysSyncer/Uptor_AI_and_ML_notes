import numpy as np
import pandas as pd
from sklearn import metrics
from math import sqrt

df = pd.read_csv("AirQualityUCI.csv", sep=";", decimal=",")
print(df.columns)
df = df.iloc[:, 0:14]
print(df.columns)

print(np.size(df))

print(df['Date'].isna().sum())
df = df[df['Date'].notnull()]
print(df['Date'].isna().sum())

print(np.size(df)) # number of Columns * number of Rows

print(df['T'])
print(df['T'].shift(5)) # Shift row towards below and adds NaN from top

df['T_t-1'] = df['T'].shift(5)

df_naive = df[['T', 'T_t-1']][5:] # From index 5
print(df_naive)

true = df_naive['T']
prediction = df_naive['T_t-1']

error = sqrt(metrics.mean_squared_error(true,prediction))
print(error)

print('RMSE for Naive Method 2: ', error)