from datetime import date
# the datetime module provides classes for manipulating dates and times, while the date class is used to represent a specific date

from prophet import Prophet
# prophet acts as a main class of this code

import streamlit as stock
# streamlit acts as a web application

import yfinance as yf
# The yfinance library is a Python library 
# for accessing financial data from Yahoo Finance, including stock market data, financial news, and historical data.

from prophet.plot import plot_plotly
# The prophet is a library for time series forecasting in Python, which is built on top of pystan.

from plotly import graph_objs as go
# plotly is a library for an interactive graph

START = "2015-01-01"
# START is assigned a string value of "2015-01-01" which represents a date in format "YYYY-MM-DD". 
# This variable is used to specify the starting date of a certain range or period of time.
TODAY = date.today().strftime("%Y-%m-%d")
# TODAY is assigned a value returned by the date.today().strftime("%Y-%m-%d") function.
# This variable is used to specify the end date of a certain range or period of time.

stock.title('Stock Prediction Application')
# Title for the streamlit application

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = stock.selectbox('Select dataset for prediction', stocks)
#Allows the user to choose the stock provided from the list.

years = stock.slider('Years of prediction:', 1, 4)
period = years * 365
# allows the user to select the number of years for which they would like to see the Stock Prediction.

@stock.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
# This function loads the historical data of a stock between a specified date range, and it uses caching to avoid loading the data again

data_load_state = stock.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('done!')
# This function only displays the loading message for the user.

stock.subheader('Raw data')
# Allows the user to see a sample of the loaded data.
stock.write(data.t())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    stock.plotly_chart(fig)
plot_raw_data()
# This code defines a function that plots the raw data of the stock prices and display it on web page.

# Predict forecast with Prophet.
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
# This code creates a new DataFrame containing only specific columns and to make it compatible with the format required by the Prophet library.

make = Prophet()
make.fit(df_train)
future = make.make_future_dataframe(periods=period)
forecast = make.predict(future)
# This code creates an instance of the Prophet class and makes a prediction for the specified number of days using the model and assign the data to the variable.

# Show and plot forecast
stock.subheader('Prediction data')
stock.write(forecast.t())

stock.write(f'Prediction plot for {years} years')
fig1 = plot_plotly(make, forecast)
stock.plotly_chart(fig1)

stock.write("Prediction components")
fig2 = make.plot_components(forecast)
stock.write(fig2)
# This code purpose is to display the stock prediction data.
