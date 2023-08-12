import numpy as np

sales_data = np.array([
    [100, 5, 10.99],
    [101, 3, 7.50],
    [102, 2, 15.99]])

prices = sales_data[:, 2]

average_price = np.mean(prices)
print(f"The average price of all products sold is: ${average_price:.2f}")
