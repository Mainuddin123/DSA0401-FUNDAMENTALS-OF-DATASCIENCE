import pandas as pd

csv_file = r"C:\Users\mainu\Downloads\customer_orders.csv"

order_data = pd.read_csv(csv_file, parse_dates=['OrderDate'], encoding='utf-8')

total_orders_by_customer = order_data.groupby('CustomerID').size()

average_order_quantity_per_product = order_data.groupby('ProductName')['OrderQuantity'].mean()

earliest_order_date = order_data['OrderDate'].min()
latest_order_date = order_data['OrderDate'].max()

print("Total Orders by Customer:\n", total_orders_by_customer)
print("\nAverage Order Quantity per Product:\n", average_order_quantity_per_product)
print("\nEarliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
