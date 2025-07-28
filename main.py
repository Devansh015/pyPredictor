# pip install streamlit fbprophet yfinance plotly
import streamlit as st
from datetime import date
import pandas as pd

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365


@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

    
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
if data.empty:
    st.error(f"Failed to download data for {selected_stock}. Try another ticker or check your internet connection.")
    st.stop()
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())



# Predict forecast with Prophet.
df_train = data[['Date','Close']].rename(columns={"Date": "ds", "Close": "y"})


# Flatten columns if needed (do this first!)

if isinstance(df_train['y'], pd.DataFrame):
    df_train['y'] = df_train['y'].iloc[:, 0]
if hasattr(df_train['ds'], 'shape') and len(df_train['ds'].shape) > 1:
    df_train['ds'] = df_train['ds'].iloc[:, 0]


# Now do type conversion
df_train['ds'] = pd.to_datetime(df_train['ds'], errors='coerce')
y_series = pd.to_numeric(df_train['y'].iloc[:, 0] if isinstance(df_train['y'], pd.DataFrame) else df_train['y'], errors='coerce')
df_train['y'] = y_series
# Always reconstruct the DataFrame before dropna
df_train = pd.DataFrame({'ds': df_train['ds'], 'y': y_series})
df_train = df_train.dropna(subset=['ds', 'y'])

if len(df_train) < 2:
    st.error("Not enough data to fit the model. Please select a different stock or date range.")
else:
    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.subheader('Forecast data')
    st.write(forecast.tail())
    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)
    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)