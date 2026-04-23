import yfinance as yf
import pandas as pd
import numpy as np
from scipy.spatial import distance

def ottieni_dati_5_fattori():
    print("Download dati in corso (Modello a 5 Fattori)...")
    # Tickers: SP500, 10Y, 3M, VIX, GOLD
    tickers = ["^GSPC", "^TNX", "^IRX", "^VIX", "GC=F"]
    
    df = yf.download(tickers, start="1995-01-01", progress=False)['Close'].copy()
    df.columns = ['Gold', 'SP500', 'Yield_10Y', 'Yield_3M', 'VIX']
    
    # Feature Engineering
    df['Curve'] = df['Yield_10Y'] - df['Yield_3M']
    df['SP500_1Y_Mom'] = df['SP500'].pct_change(periods=252) * 100
    df['Gold_1Y_Mom'] = df['Gold'].pct_change(periods=252) * 100
    df['Forward_1Y_Return'] = (df['SP500'].shift(-252) / df['SP500'] - 1) * 100
    
    return df.dropna(subset=['Curve', 'SP500_1Y_Mom', 'Gold_1Y_Mom', 'VIX'])

def analisi_avanzata(df):
    # I 5 Fattori Decisivi
    features = ['Yield_10Y', 'Curve', 'SP500_1Y_Mom', 'VIX', 'Gold_1Y_Mom']
    
    oggi = df[features].iloc[-1].values
    data_oggi = df.index[-1].strftime('%Y-%m-%d')
    
    # Pool storico (togliamo l'ultimo anno per il forecast)
    pool = df.dropna(subset=['Forward_1Y_Return']).copy()
    
    # Matrice di Covarianza Multivariata (5x5)
    cov_matrix = np.cov(pool[features].values, rowvar=False)
    cov_inv = np.linalg.inv(cov_matrix)
    
    # Scansione KNN
    distanze = pool.apply(lambda row: distance.mahalanobis(oggi, row[features].values, cov_inv), axis=1)
    pool['Distanza'] = distanze
    gemelli = pool.sort_values('Distanza').head(5)
    
    print(f"\n=== REPORT 5-FACTOR MODEL ({data_oggi}) ===")
    print(f"VIX attuale: {oggi[3]:.2f} | Gold 1Y: {oggi[4]:.2f}%")
    print("-" * 50)
    
    for i, (data, row) in enumerate(gemelli.iterrows(), 1):
        print(f"{i}. {data.date()} (Dist: {row['Distanza']:.2f}σ) -> Forward Return: {row['Forward_1Y_Return']:+.2f}%")
    
    print("-" * 50)
    print(f"FORECAST MEDIO (5 FATTORI): {gemelli['Forward_1Y_Return'].mean():+.2f}%")

if __name__ == "__main__":
    dataset = ottieni_dati_5_fattori()
    analisi_avanzata(dataset)