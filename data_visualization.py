import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("clean.csv")

df["Number of HH"] = pd.to_numeric(
    df["Number of HH"], errors="coerce"
)

df = df.dropna(
    subset=["Zone Name", "Ward name", "Number of HH"]
)

print("DATA VISUALIZATION STARTED")

# 1. Zone Wise Bar Chart
zone_data = df.groupby("Zone Name")["Number of HH"].sum()

plt.figure(figsize=(8, 5))
plt.bar(zone_data.index, zone_data.values)
plt.title("Zone Wise Household Distribution")
plt.xlabel("Zone")
plt.ylabel("Number of Households")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# 2. Zone Wise Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
    zone_data.values,
    labels=zone_data.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Household Percentage by Zone")
plt.show()

# 3. Top 10 Wards
top10 = df.nlargest(10, "Number of HH")

plt.figure(figsize=(9, 5))
plt.bar(top10["Ward name"], top10["Number of HH"])
plt.title("Top 10 Wards")
plt.xlabel("Ward Name")
plt.ylabel("Households")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Household Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Number of HH"], bins=8, edgecolor="black")
plt.title("Household Distribution")
plt.xlabel("Number of Households")
plt.ylabel("Number of Wards")
plt.show()

print("ALL VISUALIZATIONS COMPLETED!")