import pandas as pd
import numpy as np

csv_file = r"C:\Users\mainu\Downloads\Housing.csv"
df = pd.read_csv(csv_file, encoding='utf-8')

print(df.columns)

sale_price_column_name = 'price'

more_than_four_bedrooms_mask = df['bedrooms'] > 4

avg_sale_price_more_than_four_bedrooms = np.mean(df.loc[more_than_four_bedrooms_mask, sale_price_column_name])

print(f"The average sale price of houses with more than four bedrooms is: ${avg_sale_price_more_than_four_bedrooms:.2f}")
