import random
import matplotlib.pyplot as plt

static_data = [50 + i for i in range(100)]
plt.figure(figsize=[12,8])
plt.subplot(311)
plt.plot(static_data, 'o-', lable='static data', markersize=3)
plt.title('Static data')
plt.ylabel('Values')
plt.legend()

random_data = [num + random.randint(-10, 10) for num in static_data]
plt.subplot(312)
plt.plot(random_data, 'o-', lable='Random data', markersize=3)
plt.title('Data with randomness')
plt.ylabel('Values')
plt.legend()

outlier_data = random_data.copy()
for _ in range(10):
  index = random.randint(0, 99)
outlier_data[index] += random.randint(30, 50)

plt.subplot(313)
plt.plot(outlier_data, 'o-', lable='Outlier data', markersize=3)
plt.title('Data with Outlier')
plt.xlabel('Data Points')
plt.ylabel('Values')
plt.legend()

plt.tight_layout()
plt.show()

