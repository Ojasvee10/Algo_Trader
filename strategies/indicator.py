import pandas as pd
import pandas_ta as ta

def compute_indicators(df):
    df = df.copy()

    if df.empty or len(df) < 200:
        raise ValueError("DataFrame is empty or not enough rows to compute indicators.")

    df["RSI"] = ta.rsi(df["Close"], length=14)
    df["50DMA"] = df["Close"].rolling(window=50).mean()
    df["200DMA"] = df["Close"].rolling(window=200).mean()

    return df.dropna()