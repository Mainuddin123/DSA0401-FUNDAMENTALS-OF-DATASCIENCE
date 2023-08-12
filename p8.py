import pandas as pd

csv_file = r"C:\Users\mainu\Downloads\sales_data.csv"

sales_data = pd.read_csv(csv_file, parse_dates=['Date'], dayfirst=True)

product_sales = sales_data.groupby('Product')['Quantity'].sum()

sorted_products = product_sales.sort_values(ascending=False)

print("Top 5 products sold the most:")
print(sorted_products.head(5))
