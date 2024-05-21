import data_download as dd
import data_plotting as dplt
import save_data as s


def notify_if_strong_fluctuations(data, value):
    print(f'Максимальное значение цены закрытия: {max(data["Close"].round(2))}')
    print(f'Минимальное значение цены закрытия: {min(data["Close"].round(2))}')
    if max(data["Close"].round(2)) - min(data["Close"].round(2)) > value:
        print(f'Сильные колебания цены закрытия: {round((max(data["Close"]) - min(data["Close"])), 4)}')
    print()


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
    print()
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = float(input("Введите пороговое значение колебания цены: "))
    print()

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    stock_data = dd.calculate_and_display_average_price(stock_data)

    print(f'Cредняя цена закрытия акций за заданный период составляет {max(stock_data["Average_Price"].round(2))}')
    notify_if_strong_fluctuations(data=stock_data, value=threshold)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Save the data
    s.export_data_to_csv(stock_data, ticker, period)


if __name__ == "__main__":
    main()
