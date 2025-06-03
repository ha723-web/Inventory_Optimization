import pandas as pd

# Load dataset
df = pd.read_csv("inventory_data.csv")

# Flag items as overstocked or understocked
df['Status'] = df.apply(lambda row: 'Overstock' if row['Stock'] > 2 * row['Reorder_Level']
                        else ('Understock' if row['Stock'] < row['Reorder_Level'] else 'Optimal'), axis=1)

# Print result
print("\n📦 Inventory Status Report:\n")
print(df[['Item', 'Stock', 'Reorder_Level', 'Status']])
