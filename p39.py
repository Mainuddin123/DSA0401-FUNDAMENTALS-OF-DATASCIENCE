import pandas as pd
import numpy as np

data = {
    'City': ['City1', 'City1', 'City2', 'City2', 'City3'],
    'Temperature': [25.5, 27.0, 30.1, 29.8, 22.3]
}

df = pd.DataFrame(data)

mean_temperatures = df.groupby('City')['Temperature'].mean()
std_deviation_temperatures = df.groupby('City')['Temperature'].std()

temperature_ranges = df.groupby('City')['Temperature'].max() - df.groupby('City')['Temperature'].min()
city_with_highest_range = temperature_ranges.idxmax()
city_with_lowest_std_deviation = std_deviation_temperatures.idxmin()

print("Mean Temperatures:")
print(mean_temperatures)
print("\nStandard Deviations:")
print(std_deviation_temperatures)
print("\nCity with Highest Temperature Range:", city_with_highest_range)
print("City with Most Consistent Temperature:", city_with_lowest_std_deviation)
