# 🏦 Macro-Similarity Forecasting Engine (v5 Professional)

![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Macro-Similarity Forecasting Engine** è uno strumento di analisi quantitativa avanzata progettato per identificare "Gemelli Storici" nel mercato finanziario. Invece di basarsi su analisi grafiche soggettive, il sistema utilizza la **Distanza di Mahalanobis** e algoritmi di **K-Nearest Neighbors (KNN)** per misurare la somiglianza statistica tra il regime macroeconomico attuale e oltre 30 anni di dati storici.

---

## 🧠 Metodologia Quantitativa

Il motore analizza il mercato come un vettore a **5 dimensioni**, catturando le dinamiche fondamentali che guidano i cicli economici:

1.  **Costo del Denaro:** Rendimento dei Treasury USA a 10 Anni.
2.  **Rischio di Recesione:** Inversione della Curva dei Rendimenti (10Y - 3M).
3.  **Momentum Azionario:** Crescita annualizzata dell'indice S&P 500.
4.  **Sentiment/Paura:** Indice di Volatilità VIX.
5.  **Safe Haven/Inflazione:** Momentum annualizzato dell'Oro.

### Perché la Distanza di Mahalanobis?
A differenza della distanza Euclidea standard, la distanza di Mahalanobis tiene conto della **matrice di covarianza** dei dati. In finanza, le variabili sono altamente correlate; Mahalanobis "normalizza" queste relazioni, permettendo al modello di identificare somiglianze strutturali profonde anche quando i valori nominali dei prezzi sono drasticamente diversi (es. confrontare lo S&P 500 a 1.500 punti nel 2000 vs 7.000 punti nel 2026).

---

## 🚀 Caratteristiche Principali

- **ETL Automatizzato:** Integrazione diretta con le API di Yahoo Finance per dati real-time.
- **Regime Detection:** Scansione di oltre 7.500 giorni di borsa per trovare i 5 momenti storici matematicamente più simili a oggi.
- **Forecasting Probabilistico:** Calcolo del rendimento atteso a 12 mesi basato sui risultati storici dei "gemelli" individuati.
- **Dashboard Interattiva:** Interfaccia web professionale sviluppata con Streamlit per la visualizzazione immediata dei segnali.

---

## 🛠️ Installazione

1. Clona la repository:
   ```bash
   git clone [https://github.com/campolom/macro-similarity-engine.git](https://github.com/campolom/macro-similarity-engine.git)
   cd macro-similarity-engine
2. Installa le dipendenze:

Bash
pip install -r requirements.txt

3. Avvia la Dashboard:

Bash
streamlit run app.py
