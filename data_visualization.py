# DATA VISUALIZATION
# Food Waste Predictor Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the cleaned dataset
file_path = "clean.csv"
df = pd.read_csv(file_path)

# Step 2: Display dataset information
print("DATA VISUALIZATION")
print("=" * 50)

print("\nDataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# Step 3: Create output folder
os.makedirs("visualizations", exist_ok=True)

# Set visualization style
sns.set_theme(style="whitegrid")

# Step 4: Identify household-related columns
hh_columns = [
    col for col in df.columns
    if "Number of HH" in col
]

# Convert household columns to numeric
for col in hh_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ==========================================
# GRAPH 1: HOUSEHOLDS BY WARD
# ==========================================

ward_data = df.groupby("Ward name")[hh_columns[0]].sum()
ward_data = ward_data.sort_values(ascending=False)

plt.figure(figsize=(14, 6))
ward_data.plot(kind="bar")

plt.title("Households by Ward")
plt.xlabel("Ward Name")
plt.ylabel("Number of Households")
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("visualizations/households_by_ward.png")
plt.show()

# ==========================================
# GRAPH 2: HOUSEHOLDS BY ZONE
# ==========================================

zone_data = df.groupby("Zone Name")[hh_columns[0]].sum()
zone_data = zone_data.sort_values(ascending=False)

plt.figure(figsize=(9, 6))
zone_data.plot(kind="bar", color="orange")

plt.title("Households by Zone")
plt.xlabel("Zone Name")
plt.ylabel("Number of Households")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/households_by_zone.png")
plt.show()

# ==========================================
# GRAPH 3: HOUSEHOLD DISTRIBUTION BY ZONE
# ==========================================

plt.figure(figsize=(9, 6))

sns.boxplot(
    data=df,
    x="Zone Name",
    y=hh_columns[0]
)

plt.title("Household Distribution Across Zones")
plt.xlabel("Zone Name")
plt.ylabel("Number of Households")
plt.tight_layout()

plt.savefig("visualizations/household_distribution_by_zone.png")
plt.show()

# ==========================================
# GRAPH 4: TOP 10 WARDS
# ==========================================

top_wards = ward_data.head(10)

plt.figure(figsize=(10, 6))
top_wards.sort_values().plot(kind="barh", color="green")

plt.title("Top 10 Wards by Number of Households")
plt.xlabel("Number of Households")
plt.ylabel("Ward Name")
plt.tight_layout()

plt.savefig("visualizations/top_10_wards.png")
plt.show()

# ==========================================
# GRAPH 5: HOUSEHOLD VALUES COMPARISON
# ==========================================

if len(hh_columns) > 1:

    comparison_data = df[hh_columns].mean()

    plt.figure(figsize=(10, 6))
    comparison_data.plot(kind="bar", color="purple")

    plt.title("Comparison of Household Data Columns")
    plt.xlabel("Household Data Column")
    plt.ylabel("Average Value")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("visualizations/household_columns_comparison.png")
    plt.show()

# ==========================================
# GRAPH 6: HOUSEHOLDS BY ZONE - PIE CHART
# ==========================================

plt.figure(figsize=(8, 8))

zone_data.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Household Share by Zone")
plt.ylabel("")
plt.tight_layout()

plt.savefig("visualizations/household_share_by_zone.png")
plt.show()

# ==========================================
# GRAPH 7: CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(9, 6))

correlation = df[hh_columns].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Between Household Data Columns")
plt.tight_layout()

plt.savefig("visualizations/household_correlation_heatmap.png")
plt.show()

# ==========================================
# STEP 5: SUMMARY
# ==================================

