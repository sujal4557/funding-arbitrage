import streamlit as st
import requests, pandas as pd

API = "http://localhost:8000/data"

st.set_page_config(layout="wide")
st.title("📊 Funding Arbitrage Dashboard")

data = requests.get(API).json()

if not data:
    st.warning("No opportunities")
else:
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
