import geopandas
import pandas as pd

cadastre = geopandas.read_file("./data/cadastre.gpkg")

# See what’s inside
print(cadastre.head())
print(cadastre.columns)

roads = geopandas.read_file("./data/roads.gpkg")

print(roads.head())
print(roads.columns)

# gnaf_prop = geopandas.read_parquet("./data/gnaf_prop.parquet")

# print(gnaf_prop)
# print(gnaf_prop.head)

gnaf_prop = pd.read_parquet("data/gnaf_prop.parquet")
print(gnaf_prop.head())
print(gnaf_prop.columns)

transactions = pd.read_parquet("data/transactions.parquet")
print(transactions.head())
print(transactions.columns)