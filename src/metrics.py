import os
import pandas as pd

# Basvägen där detta script ligger
base_dir = os.path.dirname(__file__)
 
# Gå upp en nivå och in i data-mappen
csv_path = os.path.join(base_dir, "..", "data", "ecommerce_sales.csv")

# Läs CSV
df = pd.read_csv(csv_path)

    # Räknar genomsnittligt ordervärde (AOV)
    # AOV = Total/Antal ordrar  

def calculate_aov(df):
    total_revenue = df['revenue'].sum()
    total_orders = len(df)
    return total_revenue / total_orders

# Hämta unika produktkategorier (https://stackoverflow.com/questions/55852570/how-can-i-get-all-the-unique-categories-within-my-dataframe-using-python)
unique_category = df['category'].unique()

# skriv ut resultat
Sports_df = df[df["category"] == "Sports"]
Clothing_df = df[df["category"] == "Clothing"]
Home_df = df[df["category"] == "Home"]
Electronics_df = df[df["category"] == "Electronics"]
Toys_df = df[df["category"] == "Toys"]
Beauty_df = df[df["category"] == "Beauty"]

# Beräkna total intäkt per kategori
total_revenue = Sports_df["revenue"].sum()
print("Total intäkt för Sport kategori:", int(round(total_revenue)))
total_revenue = Clothing_df["revenue"].sum()
print("Total intäkt för clothing kategori:", int(round(total_revenue)))
total_revenue = Home_df["revenue"].sum()
print("Total intäkt för Home kategori:", int(round(total_revenue)))
total_revenue = Electronics_df["revenue"].sum()
print("Total intäkt för Electronics kategori:", int(round(total_revenue)))
total_revenue = Toys_df["revenue"].sum()
print("Total intäkt för Toys kategori:", int(round(total_revenue)))
total_revenue = Beauty_df["revenue"].sum()
print("Total intäkt för Beauty kategori:", int(round(total_revenue)))

# beräkna kategori med högst intäkt
category_revenues = {}
for kategori in unique_category:
    if kategori != "category":  # hoppa över rubriken
        kategori_df = df[df["category"] == kategori]
        total_revenue = kategori_df["revenue"].sum()
        category_revenues[kategori] = total_revenue

highest_revenue_category = max(category_revenues, key=category_revenues.get)
print("Kategori med högst intäkt:", highest_revenue_category)

# beräkna kategori med lägst intäkt
lowest_revenue_category = min(category_revenues, key=category_revenues.get)
print("Kategori med lägst intäkt:", lowest_revenue_category) 

# beräkna genomsnittlig intäkt per kategori
average_revenue = sum(category_revenues.values()) / len(category_revenues)
print("Medelvärdet av intäkter per kategori:", int(round(average_revenue)))

# Beräkna total intäkt per kategori
total_revenue_per_category = df.groupby('category')['revenue'].sum()

# Topp 3 produkter med högst intäkt 
# (https://www.reddit.com/r/learnpython/comments/16gjt3f/pandas_data_frame_selects_the_top_three_score…)
def get_top_3_categories(df):
    total_revenue_per_category = df.groupby("category")["revenue"].sum()
    top_3 = total_revenue_per_category.nlargest(3)
    return top_3
#test