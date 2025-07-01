import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("AirQualityUCI.csv", sep = ";", decimal = ",")
print(df)

df = df[df['Date'].notnull()]
print(df)

df['DateTime'] = (df.Date) + ' ' + (df.Time)
print(df)

print(type(df.DateTime[0]))
df['DateTime'] = df.DateTime.apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y %H.%M.%S'))
print(type(df.DateTime[0]))

df.index = df.DateTime
print(df)

plt.plot(df['T'])
plt.plot(df['C6H6(GT)'])
plt.boxplot(df[['T','C6H6(GT)']].values)
plt.show()