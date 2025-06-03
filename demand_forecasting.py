import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("inventory_data.csv")

# Simple 7-day demand forecast
df['7_Day_Forecast'] = df['Daily_Sales'] * 7

# Plot forecast
plt.figure(figsize=(8, 4))
plt.bar(df['Item'], df['7_Day_Forecast'], color='skyblue')
plt.title("📈 7-Day Inventory Demand Forecast")
plt.ylabel("Units")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
