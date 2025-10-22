import pandas as pd

def calculate_aov(df):
    # Beräknar genomsnittligt ordervärde (AOV)
    # AOV = Total intäkt / Antal ordrar
   
    if df.empty:
        raise ValueError("DataFrame är tom")
    
    if 'revenue' not in df.columns:
        raise ValueError("DataFrame saknar 'revenue'-kolumn")
    
    total_revenue = df['revenue'].sum()
    total_orders = len(df)
    
    return total_revenue / total_orders