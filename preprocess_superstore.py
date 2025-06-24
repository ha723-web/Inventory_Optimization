import pandas as pd
import numpy as np

# Load Superstore dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="ISO-8859-1")

# Group by product to aggregate demand info
grouped = df.groupby('Product Name').agg({
    'Quantity': 'sum',
    'Order Date': 'count'
}).reset_index()

# Rename and create necessary fields
grouped.rename(columns={'Product Name': 'Item'}, inplace=True)
grouped['Category'] = 'General'
grouped['Stock'] = grouped['Quantity'] * 1.5
grouped['Daily_Sales'] = grouped['Quantity'] / grouped['Order Date']
grouped['Reorder_Level'] = grouped['Quantity'] / 2
grouped['Lead_Time_Days'] = np.random.randint(3, 8, size=len(grouped))

# Save to CSV expected by inventory_analysis.py
final = grouped[['Item', 'Category', 'Stock', 'Daily_Sales', 'Reorder_Level', 'Lead_Time_Days']]
final.to_csv("inventory_data.csv", index=False)

print("✅ inventory_data.csv generated from Superstore dataset!")
