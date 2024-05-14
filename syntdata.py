import pandas as pd
import numpy as np
dates = pd.date_range(start='2024-01-01', end = '2024-01-10')
data= np.random.randn(10)
df = pd.DataFrame(data, index=dates, columns=['Values'])
print("Original dataframes:")
print(df)
rolling_mean =df.rolling(window=3).mean()
print("Rolling mean 3 days window")
print(rolling_mean)
weekly_average = df.resample('W').mean()
print(weekly_average)


