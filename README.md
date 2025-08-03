# 📈 Algo-Trading System with ML & Automation

This is a mini algo-trading system built in Python that fetches stock data, applies technical strategies, automates Google Sheets logging, and uses a basic ML model for predictive analytics.

---

## 🧠 Objective

- Connect to stock API (`Yahoo Finance`)
- Implement RSI + Moving Average crossover strategy
- Store trades in Google Sheets
- Analyze P&L and predictions using ML
- Bonus: Telegram alert support (optional)

---

## 🗂️ Project Structure

Algo_trader/
│
├── main.py # Entry point for the algo-system
├── config.py # Contains configurable settings (tickers, sheet name)
├── requirements.txt # Dependencies
│
├── credentials/
│ └── creds.json # Google Sheets API credentials
│
├── logs/
│ └── errors.log # Logging errors if any
│
├── services/
│ ├── data_fetcher.py # Stock data fetcher (Yahoo Finance)
│ ├── ml_model.py # Logistic Regression model
│ ├── notifier.py # Optional Telegram alert module
│ ├── sheet_logger.py # Google Sheets logging

---

## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

#Set up Google Sheets API
Place your creds.json file in credentials/ directory.

Share your Google Sheet with the service account email from the JSON.

# Run the program
bash
Copy
Edit
python -m Algo_trader.main

### 📊 Strategy Logic
Buy Signal: RSI < 30

Confirmation: 20-Day Moving Avg > 50-Day MA

Backtested over the last 6 months using Yahoo Finance data.

### 🤖 ML Model
Model: Logistic Regression

Features: RSI, MACD, Volume

Target: Predict next-day price movement (Up/Down)

Output: Accuracy shown in console

### 📋 Google Sheets Integration
Logs the following to Google Sheets:

RELIANCE.NS_Backtest : Buy/Sell signals

TCS.NS_Backtest : Summary

INFY.NS_Backtest : Ratio




