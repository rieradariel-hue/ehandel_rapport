import pandas as pd

    # Laddar e-handelsdata från CSV-fil
    # Argument:
    #     filvag: Sökväg till CSV-filen
    # Returnerar:
    #     DataFrame med sales data

def ladda_data(filvag):
    return pd.read_csv(filvag)