# main.py

import config
from services.data_fetcher import fetch_data
from strategies.strategy import backtest
from services.sheet_logger import connect_to_sheet, log_dataframe
from services.notifier import send_alert
from services.ml_model import train_predictor
import pandas as pd

def run():
    try:
        sheet = connect_to_sheet(config.GOOGLE_SHEET_NAME, config.CREDENTIALS_FILE)
    except Exception as e:
        print(f"❌ Failed to connect to Google Sheet: {e}")
        sheet = None 

    for ticker in config.TICKERS:
        try:
            print(f"\n📊 Processing {ticker}...")
            df = fetch_data(ticker, config.PERIOD, config.INTERVAL)

            # Flatten MultiIndex columns if needed
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = ['_'.join(filter(None, col)).strip() for col in df.columns.values]

            result_df = backtest(df, config.INITIAL_CAPITAL)
            print(result_df.tail(5))  # Preview recent data

            if sheet:
                log_dataframe(sheet, result_df.tail(30), f"{ticker}_Backtest")

            if "Signal" in result_df.columns:
                last_signal = result_df["Signal"].iloc[-1]
                if pd.notna(last_signal) and bool(last_signal):
                    send_alert(f"📢 Buy Signal for {ticker} ✅")

            acc = train_predictor(result_df)
            print(f"✅ Prediction accuracy for {ticker}: {acc:.2f}")

        except Exception as e:
            print(f"❌ Error while processing {ticker}: {e}")

if __name__ == "__main__":
    run()