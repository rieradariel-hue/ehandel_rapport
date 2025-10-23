import pandas as pd

#  Laddar e-handelsdata från CSV-fil (ecommerce_sales.csv)

def ladda_data(csv_fil):
    return pd.read_csv(csv_fil)