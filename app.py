import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.spatial import distance
import plotly.graph_objects as go

st.set_page_config(page_title="Quant 5-Factor Dashboard", layout="wide")

@st.cache_data
def load_data():
    tickers = ["^GSPC", "^TNX", "^IRX", "^VIX", "GC=F"]
    df = yf.download(tickers, start="1995-01-01", progress=False)['Close'].copy()
    df.columns = ['Gold', 'SP500', 'Yield_10Y', 'Yield_3M', 'VIX']
    df['Curve'] = df['Yield_10Y'] - df['Yield_3M']
    df['SP500_1Y'] = df['SP500'].pct_change(252) * 100
    df['Gold_1Y'] = df['Gold'].pct_change(252) * 100
    df['Forward_1Y'] = (df['SP500'].shift(-252) / df['SP500'] - 1) * 100
    return df.dropna(subset=['Curve', 'SP500_1Y', 'Gold_1Y', 'VIX'])

df = load_data()
features = ['Yield_10Y', 'Curve', 'SP500_1Y', 'VIX', 'Gold_1Y']
oggi = df[features].iloc[-1]

st.title("🏦 Macro-Similarity Engine (v5 Professional)")

col1, col2, col3, col4, col5 = st.columns(5)

# Usiamo i nomi esatti delle colonne invece dei numeri [0], [1], ecc.
col1.metric("10Y Yield", f"{oggi['Yield_10Y']:.2f}%")
col2.metric("Curve (bps)", f"{oggi['Curve']:.2f}")
col3.metric("S&P 500 1Y", f"{oggi['SP500_1Y']:.1f}%")
col4.metric("VIX Index", f"{oggi['VIX']:.1f}")
col5.metric("Gold 1Y", f"{oggi['Gold_1Y']:.1f}%")

# Calcolo Gemelli
pool = df.dropna(subset=['Forward_1Y']).copy()
cov_inv = np.linalg.inv(np.cov(pool[features].values, rowvar=False))
pool['Dist'] = pool.apply(lambda r: distance.mahalanobis(oggi.values, r[features].values, cov_inv), axis=1)
gemelli = pool.sort_values('Dist').head(5)

st.header("🔮 Analisi di Prossimità Storica")
st.dataframe(gemelli[features + ['Forward_1Y', 'Dist']].style.format("{:.2f}"))

forecast = gemelli['Forward_1Y'].mean()
st.sidebar.header("Forecast Risultato")
st.sidebar.subheader(f"Target 12M: {forecast:+.2f}%")