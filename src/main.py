
import os
import json
import logging

# Настройка логирования
log_file_path = os.path.join('logs', 'transactions.log')
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('utils')

def load_transactions(file_path):
    logger.info(f'Загрузка транзакций из файла: {file_path}')

    if not os.path.exists(file_path):
        logger.warning(f'Файл не существует: {file_path}')
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                logger.info('Транзакции загружены успешно')
                return data
            logger.warning('Данные в файле не являются списком')
            return []
        except json.JSONDecodeError:
            logger.error('Ошибка декодирования JSON')
            return []


import json
import pandas as pd
from transactions import filter_transactions, count_transaction_categories

def load_transactions_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_transactions_from_csv(file_path):
    return pd.read_csv(file_path, sep='\t').to_dict(orient='records')

def load_transactions_from_xlsx(file_path):
    return pd.read_excel(file_path, engine='openpyxl').to_dict(orient='records')

def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    choice = input("Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n")

    # Загрузка файл и выбор статуса
    if choice == '1':
        transactions = load_transactions_from_json('transactions.json')
    elif choice == '2':
        transactions = load_transactions_from_csv('transactions.csv')
    elif choice == '3':
        transactions = load_transactions_from_xlsx('transactions.xlsx')
    else:
        print("Неверный выбор!")
        return

    status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").lower()
    valid_statuses = ['executed', 'canceled', 'pending']

    while status not in valid_statuses:
        print(f"Статус операции \"{status}\" недоступен.")
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").lower()

    print(f"Программа: Операции отфильтрованы по статусу \"{status.upper()}\"")

    # Фильтрация по статусу
    filtered_transactions = [t for t in transactions if t['state'].lower() == status]

    sort_option = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_option == "да":
        order = input("Сортировать по возрастанию или по убыванию? \n").strip().lower()
        if order == "по возрастанию":
            filtered_transactions.sort(key=lambda t: t['date'])
        elif order == "по убыванию":
            filtered_transactions.sort(key=lambda t: t['date'], reverse=True)

    currency_filter = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if currency_filter == "да":
        filtered_transactions = [t for t in filtered_transactions if t['currency_name'] == 'рубль']

    description_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if description_filter == "да":
        search_string = input("Введите строку для поиска в описании:\n")
        filtered_transactions = filter_transactions(filtered_transactions, search_string)

    # Вывод результата
    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{transaction['date']} {transaction['description']}\nСчет {transaction['from']} -> Счет {transaction['to']}\nСумма: {transaction['amount']} {transaction['currency_name']}\n")
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

if __name__ == "__main__":
    main()