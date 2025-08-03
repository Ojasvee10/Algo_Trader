import yfinance as yf
import pandas as pd

def fetch_data(ticker, period="60d", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]

    return df