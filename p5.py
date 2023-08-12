import numpy as np
import pandas as pd

csv_file = r"C:\Users\mainu\Downloads\fuel_efficiency.csv"
df = pd.read_csv(csv_file, encoding='utf-8')

fuel_efficiency_column_name = 'Fuel efficiency(mpg)'
fuel_efficiency = df[fuel_efficiency_column_name].values

average_fuel_efficiency = np.mean(fuel_efficiency)

model1_efficiency = fuel_efficiency[0]
model2_efficiency = fuel_efficiency[-1]

percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100

print(f"Average Fuel Efficiency: {average_fuel_efficiency:.2f} mpg")
print(f"Percentage Improvement between Model 1 and Model 2: {percentage_improvement:.2f}%")
