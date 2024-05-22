import matplotlib.pyplot as plt
import pandas as pd
import save_data as sd
import plotly.graph_objects as go


def create_and_save_plot(data, ticker, period, start, end):
    # print(plt.style.available) # список доступных стилей
    theme = input('Укажите стиль оформления графика: ')
    plt.style.use(theme)
    plt.figure(figsize=(12, 6))
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['Average_Price'].values, label='Average Volume')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['Average_Price'], label='Average Volume')
    plt.title(f"{ticker.upper()} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
    filename = f'{sd.determine_filename(ticker, period, start, end)} stock_price_chart.png'
    plt.savefig(filename)
    print(f'График цен закрытия, скользящего среднего и средней цены сохранен как {filename}')


def plot_macd(data, ticker, period, start, end):
    theme = input('Укажите стиль оформления графика MACD: ')
    plt.style.use(theme)
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['MACD_12_26_9'], label='MACD', color='blue')
    plt.plot(data.index, data['MACDs_12_26_9'], label='Signal Line', color='red')
    plt.bar(data.index, data['MACDh_12_26_9'], label='MACD Histogram', color='grey')
    plt.title(f'MACD {ticker.upper()}')
    plt.legend(loc='upper left')
    filename = f'{sd.determine_filename(ticker, period, start, end)} macd_chart.png'
    plt.savefig(filename)
    print(f'График MACD сохранен как {filename}')


def plot_rsi(data, ticker, period, start, end):
    theme = input('Укажите стиль оформления графика RSI: ')
    plt.style.use(theme)
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['RSI'], label='RSI', color='orange')
    plt.axhline(y=70, color='red', linestyle='--')
    plt.axhline(y=30, color='green', linestyle='--')
    plt.title(f'RSI {ticker.upper()}')
    plt.legend(loc='upper left')
    filename = f"{sd.determine_filename(ticker, period, start, end)} rsi_chart.png"
    plt.savefig(filename)
    print(f'График RSI сохранен как {filename}')


def plot_std_dev(data, ticker, period, start, end):
    theme = input('Укажите стиль оформления графика стандартного отклонения: ')
    plt.style.use(theme)
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Std_Dev'], label='Standard Deviation', color='purple')
    plt.title(f'Standard Deviation {ticker.upper()}')
    plt.legend(loc='upper left')
    filename = f"{sd.determine_filename(ticker, period, start, end)} std_dev_chart.png"
    plt.savefig(filename)
    print(f'График стандартного отклонения сохранен как {filename}')


def interactive_plot(data, ticker):
    fig = go.Figure(data=[go.Scatter(x=data.index, y=data['Close'])])
    fig.update_layout(title=f"Цена закрытия акций {ticker.upper()}", xaxis_title="Дата закрытия", yaxis_title="Цена закрытия")
    fig.show()