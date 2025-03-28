def filter_by_currency(transactions, currency_code):
    """Генератор, который фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    """Генератор, который возвращает описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction['description']

def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в заданном диапазоне."""
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]