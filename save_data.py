def export_data_to_csv(data, ticker, period, start, end):
    try:
        filename = f'{determine_filename(ticker=ticker, start_date=start, end_date=end, period=period)}.csv'
        data.to_csv(filename)
        print(f'Данные успешно сохранены в файл {filename}')
    except Exception as e:
        print(f'Возникла ошибка при сохранении данных в файл CSV: {e}')


def determine_filename(ticker, period=None, start_date=None, end_date=None ):
    if start_date and end_date:
        filename = f"{ticker} {start_date} - {end_date}"
    elif period:
        filename = f"{ticker} {period}"
    return filename
