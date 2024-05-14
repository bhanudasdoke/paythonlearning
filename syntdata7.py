import pandas as pd
from faker import Faker
import numpy as np
from datetime import datetime

faker = Faker()

def generate_data(num_records):
    data = {'Name': [], 'Age': [], 'Email': [], 'Hight': [], 'Weight': [] }
    for _ in range(num_records):
        data['Name'].append(faker.name())
        data['Email'].append(faker.email())
        data['Age'].append(np.random.randint(18.70))
        data['Hight'].append(np.random.randint(150.195))
        data['Weight'].append(np.random.randint(50.100))

        return pd.DataFrame(data)
df = generate_data(2000)

processed_df = df[(df['Age'] > 20) & (df['Age'] < 50)]

unique_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

processed_df.to_csv(f'data_{unique_timestamp}.csv', index=False)

