import pandas as pd
from faker import Faker
import numpy as np
#from pandasgui import show

faker = Faker
df = pd.DataFrame()
df['Name'] = [faker.name() for _ in range(100)]
df['Address'] = [faker.address() for _ in range(100)]
df['Age'] = np.random.normal(30, 10, 100).astype(int)
df['Hight'] = np.random.normal(170, 10, 100).astype(int)
df['Weight'] = np.random.normal(70, 15, 100).astype(int)

df['Email'] = [faker.email() for _ in range(100)]
df['Car Registration'] = [faker.bothify(text='?###???') for _ in range(100)]

df['PAN'] = [faker.bothify(text='?????####?') for _ in range(100)]

print(df)



