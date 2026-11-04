# ============================================
# DATA ANALYSIS PROJECT - WARANGAL HOUSEHOLDS
# ============================================

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 2: Load the cleaned dataset
file_path = "clean.csv"

if not os.path.exists(file_path):
    print("Error: clean.csv file not found!")
    print("Please keep clean.csv in the same folder as this Python file.")
    exit()

df = pd.read_csv(file_path)

print("=" * 60)
print("       WARANGAL HOUSEHOLD DATA ANALYSIS")
print("=" * 60)

# Step 3: Display basic information
print("\n1. DATASET INFORMATION")
print("-" * 40)

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Preview:")
print(df.head())

print("\nDataset Information:")
df.info()

# Step 4: Check missing values
print("\n2. MISSING VALUES ANALYSIS")
print("-" * 40)

print(df.isnull().sum())

# Step 5: Check duplicate records
print("\n3. DUPLICATE RECORD ANALYSIS")
print("-" * 40)

print("Duplicate Rows:", df.duplicated().sum())

# Step 6: Statistical analysis
# Use the primary household-number column
household_column = "Number of HH"

print("\n4. STATISTICAL DATA ANALYSIS")
print("-" * 40)

print(df[household_column].describe())

print("\nTotal Households:")
print(df[household_column].sum())

print("\nAverage Households per Ward:")
print(round(df[household_column].mean(), 2))

print("\nMaximum Households:")
print(df[household_column].max())

print("\nMinimum Households:")
print(df[household_column].min())

print("\nMedian Households:")
print(df[household_column].median())

# Step 7: Zone-wise analysis
print("\n5. ZONE-WISE HOUSEHOLD ANALYSIS")
print("-" * 40)

zone_analysis = df.groupby("Zone Name").agg(
    Total_Households=("Number of HH", "sum"),
    Average_Households=("Number of HH", "mean"),
    Number_of_Wards=("Ward name", "count")
).round(2)

print(zone_analysis)

# Step 8: Find the ward with the highest households
print("\n6. HIGHEST HOUSEHOLD WARD")
print("-" * 40)

highest_ward = df.loc[df[household_column].idxmax()]

print("Ward Name:", highest_ward["Ward name"])
print("Zone Name:", highest_ward["Zone Name"])
print("Households:", highest_ward[household_column])

# Step 9: Find the ward with the lowest households
print("\n7. LOWEST HOUSEHOLD WARD")
print("-" * 40)

lowest_ward = df.loc[df[household_column].idxmin()]

print("Ward Name:", lowest_ward["Ward name"])
print("Zone Name:", lowest_ward["Zone Name"])
print("Households:", lowest_ward[household_column])

# Step 10: Sort wards by household count
print("\n8. TOP 10 WARDS BY HOUSEHOLD COUNT")
print("-" * 40)

top_wards = df.sort_values(
    by=household_column,
    ascending=False
).head(10)

print(top_wards[["Ward name", "Zone Name", household_column]])

# Step 11: Save analysis results
output_folder = "analysis_results"
os.makedirs(output_folder, exist_ok=True)

zone_analysis.to_csv(
    os.path.join(output_folder, "zone_analysis.csv")
)

top_wards.to_csv(
    os.path.join(output_folder, "top_10_wards.csv"),
    index=False
)

df.describe().to_csv(
    os.path.join(output_folder, "statistical_summary.csv")
)

print("\nAnalysis results saved in the analysis_results folder.")

# Step 12: Visualization 1 - Households by Ward
plt.figure(figsize=(15, 6))

plt.bar(
    df["Ward name"],
    df[household_column]
)

plt.title("Household Distribution by Ward")
plt.xlabel("Ward Name")
plt.ylabel("Number of Households")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(
    os.path.join(output_folder, "households_by_ward.png")
)
plt.show()

# Step 13: Visualization 2 - Total Households by Zone
zone_totals = df.groupby("Zone Name")[household_column].sum()

plt.figure(figsize=(9, 5))

plt.bar(
    zone_totals.index,
    zone_totals.values
)

plt.title("Total Households by Zone")
plt.xlabel("Zone Name")
plt.ylabel("Total Households")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(
    os.path.join(output_folder, "households_by_zone.png")
)
plt.show()

# Step 14: Visualization 3 - Average Households by Zone
zone_averages = df.groupby("Zone Name")[household_column].mean()

plt.figure(figsize=(9, 5))

plt.bar(
    zone_averages.index,
    zone_averages.values
)

plt.title("Average Households per Ward by Zone")
plt.xlabel("Zone Name")
plt.ylabel("Average Households")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(
    os.path.join(output_folder, "average_households_by_zone.png")
)
plt.show()

# Step 15: Visualization 4 - Household Distribution
plt.figure(figsize=(9, 5))

plt.hist(
    df[household_column],
    bins=10,
    edgecolor="black"
)

plt.title("Distribution of Households Across Wards")
plt.xlabel("Number of Households")
plt.ylabel("Number of Wards")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(
    os.path.join(output_folder, "household_distribution.png")
)
plt.show()

# Step 16: Final summary
print("\n9. FINAL DATA ANALYSIS SUMMARY")
print("-" * 40)

print("Total Number of Wards:", df["Ward name"].nunique())
print("Total Number of Zones:", df["Zone Name"].nunique())
print("Total Households:", df[household_column].sum())
print(
    "Average Households per Ward:",
    round(df[household_column].mean(), 2)
)
print("Highest Household Ward:", highest_ward["Ward name"])
print("Lowest Household Ward:", lowest_ward["Ward name"])

print("\nDATA ANALYSIS COMPLETED SUCCESSFULLY!")

