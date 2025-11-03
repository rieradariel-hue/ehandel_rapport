from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).parent      # src/
csv_path = base_dir.parent / "data" / "ecommerce_sales.csv"

df = pd.read_csv(csv_path)

total_revenue = df["revenue"].sum()
total_units = df["units"].sum()

# print(int(round(total_revenue)))

# code for cities name 

sales_cities = df['city'].to_list()

unique_cities = []

# Loop through and add only new cities
for city in sales_cities:
    if city not in unique_cities:
        unique_cities.append(city)

city_sales = df.groupby('city')['revenue'].sum().sort_values(ascending=False) # kaggle.com

max_city = city_sales.idxmax()
max_sales = city_sales.max()

print(unique_cities) 
print(f"The city with the highest total sales is {max_city} with total revenue of {max_sales: .2f} SEK")

plt.figure(figsize=(10,6))
plt.bar(city_sales.index, city_sales.values)
plt.title('Total försäljning per stad')
plt.xlabel('Stad')
plt.ylabel('Total försäljning')
plt.show()