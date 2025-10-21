import pandas as pd

def calculate_aov(df):
    # Beräknar genomsnittligt ordervärde (AOV)
    # AOV = Total intäkt / Antal ordrar
    # Argument:
    #   df: DataFrame med orderdata som innehåller 'revenue'-kolumn
    # Returnerar:
    #   float: Genomsnittligt ordervärde
    
    # Validering - kontrollera att DataFrame inte är tom
    if df.empty:
        raise ValueError("DataFrame är tom")
    
    # Validering - kontrollera att 'revenue'-kolumnen finns
    if 'revenue' not in df.columns:
        raise ValueError("DataFrame saknar 'revenue'-kolumn")
    
    # Beräkna total intäkt från alla ordrar
    total_revenue = df['revenue'].sum()
    
    # Räkna totalt antal ordrar (varje rad representerar en order)
    total_orders = len(df)
    
    # Beräkna och returnera genomsnittligt ordervärde
    aov = total_revenue / total_orders
    return aov