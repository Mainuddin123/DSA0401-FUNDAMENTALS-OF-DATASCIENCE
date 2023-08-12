import pandas as pd
data={'Property Id':[1,2,3,4,5],
      'Location':['city A','city B','city A','city C','city B'],
      'Number of Bedrooms':[3,4,2,5,3],
      'Area(sqft)':[1500,2000,1200,2500,1800],
      'Listing Price':[250000,350000,180000,500000,300000]}

property_data=pd.DataFrame(data)
average_price_by_location=property_data.groupby('Location')['Listing Price'].mean()
print("Avearge listing price by location:")
print(average_price_by_location)

num_properties_with_more_than_four_bedrooms=(property_data['Number of Bedrooms']>4).sum()
print("Number of properties with more than four Bedrooms:",num_properties_with_more_than_four_bedrooms)
property_with_largest_area=property_data[property_data['Area(sqft)']==property_data['Area(sqft)'].max()]
print("Property_with_largest Area:",property_with_largest_area)
