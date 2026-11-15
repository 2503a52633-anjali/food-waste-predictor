import pandas as pd

# Load cleaned dataset
df = pd.read_csv("clean.csv")

print("\n========== DATA ANALYTICS ==========")

# Basic information
print("\n1. DATASET INFORMATION")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
print("Total Wards:", df["Ward name"].nunique())
print("Total Zones:", df["Zone Name"].nunique())

# Household analysis
df["Number of HH"] = pd.to_numeric(df["Number of HH"], errors="coerce")

print("\n2. HOUSEHOLD ANALYSIS")
print("Total Households:", df["Number of HH"].sum())
print("Average Households:", round(df["Number of HH"].mean(), 2))
print("Maximum Households:", df["Number of HH"].max())
print("Minimum Households:", df["Number of HH"].min())

# Zone-wise analysis
print("\n3. ZONE-WISE ANALYSIS")

zone_analysis = df.groupby("Zone Name")["Number of HH"].agg(
    ["count", "sum", "mean", "min", "max"]
)

zone_analysis.columns = [
    "Total Wards",
    "Total Households",
    "Average Households",
    "Minimum",
    "Maximum"
]

print(zone_analysis)

# Top 10 wards
print("\n4. TOP 10 WARDS")

top_wards = df.nlargest(10, "Number of HH")

print(top_wards[["Ward name", "Zone Name", "Number of HH"]])

# Bottom 10 wards
print("\n5. BOTTOM 10 WARDS")

bottom_wards = df.nsmallest(10, "Number of HH")

print(bottom_wards[["Ward name", "Zone Name", "Number of HH"]])


print("\nDATA ANALYTICS COMPLETED SUCCESSFULLY!")