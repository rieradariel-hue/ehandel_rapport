from pathlib import Path
import pandas as pd

base_dir = Path(__file__).parent      # src/
csv_path = base_dir.parent / "data" / "ecommerce_sales.csv"

df = pd.read_csv(csv_path)

total_revenue = df["revenue"].sum()
total_units = df["units"].sum()

# print(int(round(total_revenue)))
#12345