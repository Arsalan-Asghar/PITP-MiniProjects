# Week 6 - Mini Project 1 - Analyzing and Visualizing Sales Data:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Data Cleaning
df.fillna({"Sales": df["Sales"].mean(), "Quantity": df["Quantity"].median()}, inplace=True)
df.dropna(subset=["Product"], inplace=True)
df.drop_duplicates(inplace=True)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

print(df.info())
print(df.head())

# Sales Over Time
plt.figure(figsize=(10, 5))
df.groupby("Date")["Sales"].sum().plot()
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales Over Time")
plt.grid()
plt.show()

# Top 5 Best-Selling Products
top_products = df.groupby("Product")["Sales"].sum().nlargest(5)
plt.figure(figsize=(8, 4))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.title("Top 5 Best-Selling Products")
plt.show()

# Sales Distribution by Region
plt.figure(figsize=(8, 5))
sns.boxplot(x="Region", y="Sales", data=df)
plt.title("Sales Distribution Across Regions")
plt.xticks(rotation=45)
plt.show()