import pandas as pd
import matplotlib.pyplot as plt
import textwrap

# Load the processed inventory dataset
df = pd.read_csv("inventory_data.csv")

# Calculate 7-day demand forecast
df['7_Day_Forecast'] = df['Daily_Sales'] * 7

# Sort and select top 20 SKUs with highest forecast
top20 = df.sort_values(by='7_Day_Forecast', ascending=False).head(20)


# Wrap item names nicely
top20['Item'] = top20['Item'].apply(lambda x: '\n'.join(textwrap.wrap(x, width=25)))

# Plot with more space and smaller font
plt.figure(figsize=(12, 14))
bars = plt.barh(top20['Item'], top20['7_Day_Forecast'], color='skyblue')

plt.xlabel("Units", fontsize=12)
plt.ylabel("Item", fontsize=12)
plt.title("🔮 Top 20 SKUs by 7-Day Inventory Demand Forecast", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=8)
plt.gca().invert_yaxis()  # Show largest at top
plt.tight_layout(pad=3.0)
plt.savefig("top20_forecast_horizontal.png")
plt.show()


# Optional: Print table in terminal
print("\n📦 Top 20 Forecast Summary:\n")
print(top20[['Item', 'Stock', 'Reorder_Level', '7_Day_Forecast']])
