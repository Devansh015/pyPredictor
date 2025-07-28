# 📊 Stock Forecast App

A simple and interactive **Stock Forecasting Web App**.

## Features

-  Select from a list of major stocks (GOOG, AAPL, MSFT, GME)
-  Automatically fetches historical stock price data using the Yahoo Finance API
-  Performs future forecasting using Facebook Prophet
-  Displays forecast plots and component trends up to 4 years
-  Interactive UI with sliders and dropdowns

##  Built With

- [Streamlit](https://streamlit.io/) – for creating the web app UI
- [Facebook Prophet](https://facebook.github.io/prophet/) – for time series forecasting
- [yfinance](https://github.com/ranaroussi/yfinance) – for fetching stock market data
- [Pandas](https://pandas.pydata.org/) – for data handling and cleaning

##  Getting Started

Follow these steps to get the app up and running locally:

### 1.  Clone the Repository

```bash
git clone https://github.com/Devansh015/pyPredictor.git
```

### 2. Cd into project folder
```bash

cd pyPredictor
```

### 3. Install Dependencies

```bash
pip install streamlit prophet yfinance plotly
```
### 4. Run with
```bash
streamlit run app.py
```
