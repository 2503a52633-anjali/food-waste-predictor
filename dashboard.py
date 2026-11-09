"""Interactive Food Waste data dashboard (Streamlit)."""
from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "cleaned_food_waste.csv"

st.set_page_config(page_title="Food Waste Predictor", page_icon="♻️", layout="wide")
st.title("♻️ Food Waste Predictor – Data Dashboard")
st.caption("Exploratory dashboard built from the supplied Food Waste dataset.")

@st.cache_data
def load_data():
    if not DATA_FILE.exists():
        return None
    data = pd.read_csv(DATA_FILE)
    data["FlowAmount"] = pd.to_numeric(data["FlowAmount"], errors="coerce")
    return data.dropna(subset=["FlowAmount"])

data = load_data()
if data is None:
    st.error("cleaned_food_waste.csv not found. Run: python data_cleaning.py")
    st.stop()
if data.empty:
    st.warning("No usable Food Waste records found in the cleaned dataset.")
    st.stop()

filtered = data.copy()
filter_cols = st.columns(3)

if "Class" in filtered and filtered["Class"].notna().any():
    options = sorted(filtered["Class"].dropna().astype(str).unique())
    selected = filter_cols[0].multiselect("Class", options, default=options)
    filtered = filtered[filtered["Class"].astype(str).isin(selected)]

if "SectorProducedBy" in filtered and filtered["SectorProducedBy"].notna().any():
    options = sorted(filtered["SectorProducedBy"].dropna().astype(str).unique())
    selected = filter_cols[1].multiselect("Produced by sector code", options)
    if selected:
        filtered = filtered[filtered["SectorProducedBy"].astype(str).isin(selected)]

if "SectorConsumedBy" in filtered and filtered["SectorConsumedBy"].notna().any():
    options = sorted(filtered["SectorConsumedBy"].dropna().astype(str).unique())
    selected = filter_cols[2].multiselect("Consumed by sector code", options)
    if selected:
        filtered = filtered[filtered["SectorConsumedBy"].astype(str).isin(selected)]

unit = str(filtered["Unit"].dropna().iloc[0]) if "Unit" in filtered and filtered["Unit"].notna().any() else "reported units"
total = filtered["FlowAmount"].sum()
avg = filtered["FlowAmount"].mean()
k1, k2, k3 = st.columns(3)
k1.metric("Records", f"{len(filtered):,}")
k2.metric(f"Total flow ({unit})", f"{total:,.2f}")
k3.metric(f"Average flow ({unit})", f"{avg:,.2f}")

left, right = st.columns(2)
with left:
    if "SectorProducedBy" in filtered:
        st.subheader("Top producing sector codes")
        chart = filtered.groupby("SectorProducedBy")["FlowAmount"].sum().nlargest(10)
        st.bar_chart(chart)
with right:
    if "SectorConsumedBy" in filtered:
        st.subheader("Top consuming sector codes")
        chart = filtered.groupby("SectorConsumedBy")["FlowAmount"].sum().nlargest(10)
        st.bar_chart(chart)

if "Class" in filtered:
    st.subheader("Food waste flow by class")
    st.bar_chart(filtered.groupby("Class")["FlowAmount"].sum().sort_values(ascending=False))

st.subheader("Filtered data")
st.dataframe(filtered, use_container_width=True)

st.info(
    "Prediction limitation: the supplied file contains records for only one year (2018) "
    "and one location code. It does not provide a time series for training or validating "
    "future-year predictions. This dashboard therefore reports and explores the supplied "
    "data; a reliable forecasting model requires additional years and suitable target data."
)
