def export_data_to_csv(data, tiker, period, filename=None):
    try:
        if filename is None:
            filename = f'{tiker}_{period}_stocks.csv'
        data.to_csv(filename)
        print(f'Данные успешно сохранены в файл {filename}')
    except Exception as e:
        print(f'Возникла ошибка при сохранении данных в файл CSV: {e}')
