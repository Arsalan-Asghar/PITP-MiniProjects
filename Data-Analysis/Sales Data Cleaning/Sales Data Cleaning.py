# Week 7 - Mini Project 1 - Analyzing and Visualizing Sales Data:

import pandas as pd

file_path = 'sales_data.csv'
df = pd.read_csv(file_path)

print("Before Cleaning:")
print(df.info())

# Handle Missing Data
df.fillna(df.mean(numeric_only=True), inplace=True)
if 'Product Name' in df.columns:
    df.dropna(subset=['Product Name'], inplace=True)

df.drop_duplicates(inplace=True)

# Convert Data Types
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

num_cols = df.select_dtypes(include=['object']).columns
for col in num_cols:
    try:
        df[col] = pd.to_numeric(df[col])
    except ValueError:
        pass

print("\nAfter Cleaning:")
print(df.info())

df.to_csv('cleaned_sales_data.csv', index=False)
print("Cleaned dataset saved as 'cleaned_sales_data.csv'.")