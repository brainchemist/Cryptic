import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Crypto Dashboard")

st.title("📊 Crypto Price Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("prices.csv", names=["timestamp", "coin", "price", "change"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["price"] = df["price"].astype(float)
    return df

df = load_data()

# Coin selector
coin = st.selectbox("Select coin:", df["coin"].unique())

# Filter data
filtered = df[df["coin"] == coin]

# Display chart
st.line_chart(filtered.set_index("timestamp")["price"])

# Show raw data
with st.expander("Show data"):
    st.dataframe(filtered.sort_values(by="timestamp", ascending=False))
