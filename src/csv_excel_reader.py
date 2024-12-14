import csv
import pandas as pd


def read_transactions_from_csv(file_path):
    # Чтение данных из CSV файла
    df = pd.read_csv(file_path)
    # Преобразование данных в список словарей
    transactions = df.to_dict(orient='records')
    return transactions


def read_transactions_from_excel(file_path):
    # Чтение данных из Excel файла
    df = pd.read_excel(file_path)
    # Преобразование данных в список словарей
    transactions = df.to_dict(orient='records')
    return transactions


# Указание путей к файлам
csv_file = 'path/to/transactions.csv'
excel_file = 'path/to/transactions_excel.xlsx'

# Чтение транзакций
csv_transactions = read_transactions_from_csv(csv_file)
excel_transactions = read_transactions_from_excel(excel_file)

# Вывод результатов
print(csv_transactions)
print(excel_transactions)





