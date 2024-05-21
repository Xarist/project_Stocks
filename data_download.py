import yfinance as yf
# import pandas as pd
import pandas_ta as ta


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    data['Average_Price'] = data['Close'].mean()
    return data


def calculate_rsi(data, window_size=14):
    data['RSI'] = ta.rsi(data['Close'], window=window_size)
    return data


def calculate_macd(data):
    data_macd = data.ta.macd(close='Close', fast=12, slow=26, signal=9, append=True)
    return data
