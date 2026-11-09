"""Create charts from the cleaned Food Waste dataset."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "cleaned_food_waste.csv"
OUTPUT_DIR = BASE_DIR / "charts"

def main():
    data = pd.read_csv(DATA_FILE)
    data["FlowAmount"] = pd.to_numeric(data["FlowAmount"], errors="coerce")
    data = data.dropna(subset=["FlowAmount"])
    OUTPUT_DIR.mkdir(exist_ok=True)

    if "Class" in data and data["Class"].notna().any():
        values = data.groupby("Class")["FlowAmount"].sum().sort_values(ascending=False).head(12)
        ax = values.plot(kind="bar", title="Food Waste Flow Amount by Class")
        ax.set_xlabel("Class")
        ax.set_ylabel("Flow amount")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "flow_by_class.png", dpi=160)
        plt.close()

    for column, filename, title, xlabel in [
        ("SectorProducedBy", "top_producing_sectors.png", "Top Producing Sector Codes", "Sector code"),
        ("SectorConsumedBy", "top_consuming_sectors.png", "Top Consuming Sector Codes", "Sector code"),
    ]:
        if column in data:
            values = data.groupby(column)["FlowAmount"].sum().nlargest(10)
            ax = values.plot(kind="bar", title=title)
            ax.set_xlabel(xlabel)
            ax.set_ylabel("Flow amount")
            plt.tight_layout()
            plt.savefig(OUTPUT_DIR / filename, dpi=160)
            plt.close()

    print(f"Charts saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
