"""Summary analytics for the Food Waste dataset."""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "cleaned_food_waste.csv"

def load_data(path=DATA_FILE):
    data = pd.read_csv(path)
    data["FlowAmount"] = pd.to_numeric(data["FlowAmount"], errors="coerce")
    return data.dropna(subset=["FlowAmount"])

def run_analysis():
    data = load_data()
    print("\nFOOD WASTE DATASET SUMMARY")
    print("-" * 45)
    print(f"Records: {len(data):,}")
    print(f"Total reported flow: {data['FlowAmount'].sum():,.2f} {data['Unit'].dropna().iloc[0] if 'Unit' in data and data['Unit'].notna().any() else ''}")
    print(f"Average flow per record: {data['FlowAmount'].mean():,.2f}")
    if "Year" in data:
        print(f"Years present: {sorted(data['Year'].dropna().unique().tolist())}")
    if "Location" in data:
        print(f"Locations present: {data['Location'].nunique(dropna=True)}")

    if "SectorProducedBy" in data:
        print("\nTop producing sectors (sector codes):")
        print(data.groupby("SectorProducedBy")["FlowAmount"].sum().nlargest(10).to_string())
    if "SectorConsumedBy" in data:
        print("\nTop consuming sectors (sector codes):")
        print(data.groupby("SectorConsumedBy")["FlowAmount"].sum().nlargest(10).to_string())
    if "Class" in data:
        print("\nFlow amount by class:")
        print(data.groupby("Class")["FlowAmount"].sum().sort_values(ascending=False).to_string())

if __name__ == "__main__":
    run_analysis()
