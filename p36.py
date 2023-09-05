import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
num_days = 100
closing_prices = np.random.normal(100, 5, num_days)

data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=num_days, freq='D'),
    'Closing_Price': closing_prices
})

data['Daily_Return'] = data['Closing_Price'].pct_change() * 100

std_deviation = data['Daily_Return'].std()
mean_return = data['Daily_Return'].mean()
max_return = data['Daily_Return'].max()
min_return = data['Daily_Return'].min()

plt.hist(data['Daily_Return'].dropna(), bins=30, alpha=0.75, color='blue')
plt.xlabel('Daily Return (%)')
plt.ylabel('Frequency')
plt.title('Histogram of Daily Returns')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Closing_Price'], marker='o', linestyle='-', color='green')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Prices Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

print(f'Standard Deviation of Daily Returns: {std_deviation:.2f}%')
print(f'Mean Daily Return: {mean_return:.2f}%')
print(f'Max Daily Return: {max_return:.2f}%')
print(f'Min Daily Return: {min_return:.2f}%')
