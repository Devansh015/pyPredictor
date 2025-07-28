# 📊 Stock Forecast App

A simple and interactive **Stock Forecasting Web App**.

## ✨ Features

- ✅ Select from a list of major stocks (GOOG, AAPL, MSFT, GME)
- 🔄 Automatically fetches historical stock price data using the Yahoo Finance API
- 🔮 Performs future forecasting using Facebook Prophet
- 📊 Displays forecast plots and component trends up to 4 years
- 🧩 Interactive UI with sliders and dropdowns

## 🛠 Built With

- [Streamlit](https://streamlit.io/) – for creating the web app UI
- [Facebook Prophet](https://facebook.github.io/prophet/) – for time series forecasting
- [yfinance](https://github.com/ranaroussi/yfinance) – for fetching stock market data
- [Pandas](https://pandas.pydata.org/) – for data handling and cleaning

## 📦 Installation

```bash
pip install streamlit prophet yfinance plotly
```
## Run with
streamlit run app.py
