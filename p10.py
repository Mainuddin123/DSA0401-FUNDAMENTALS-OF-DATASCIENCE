import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [50000, 60000, 75000, 80000, 90000, 100000]

plt.figure(figsize=(8,6))
plt.plot(months, sales_values, marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.bar(months, sales_values, color='r', align='center', alpha=0.7)
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.grid(True)
plt.show()
