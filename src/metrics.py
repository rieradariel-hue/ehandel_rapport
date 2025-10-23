import pandas as pd

    # Räknar genomsnittligt ordervärde (AOV)
    # AOV = Total/Antal ordrar  

def calculate_aov(df):
    total_revenue = df['revenue'].sum()
    total_orders = len(df)
    return total_revenue / total_orders