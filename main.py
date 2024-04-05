import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read data from CSV files
data1 = pd.read_csv("data1.csv")
data2 = pd.read_csv("data2.csv")
data3 = pd.read_csv("data3.csv")

# Explore data
print("Data1 Info:")
print(data1.info())
print("\nData2 Info:")
print(data2.info())
print("\nData3 Info:")
print(data3.info())


# Cleaning data
data1_cleaned = data1.dropna()
data2_cleaned = data2.dropna()
data3_cleaned = data3.dropna()


# Manipulate data
data1_cleaned["Total Sales"] = data1_cleaned["Sales1"] + data1_cleaned["Sales2"]

# Merge data
merged_data = pd.merge(data1_cleaned, data2_cleaned, on="ID", how="inner")


# Join data
joined_data = merged_data.join(data3_cleaned.set_index("ID"), on="ID")

# # visualize data
# Based on Region
plt.figure(figsize=(8, 6))
plt.bar(joined_data["Region"], joined_data["Total Sales"])
plt.xlabel("Pulau")
plt.ylabel("Total Penjualan")
plt.title("Total Penjualan Berdasarkan Pulau")
plt.savefig("total_penjualan.png")

# Based on product
product_sales = joined_data.groupby("Product")["Total Sales"].sum()
plt.figure(figsize=(8, 6))
plt.bar(product_sales.index, product_sales.values)
plt.xlabel("Product")
plt.ylabel("Total Penjualan")
plt.title("Total Penjualan by Product")
plt.tight_layout()  # Adjust spacing
plt.savefig("total_harga.png")
