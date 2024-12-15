import re
from collections import Counter

def filter_transactions(transactions, search_string):
    """Фильтрует список транзакций по строке поиска в описании с использованием регулярных выражений."""
    pattern = re.compile(search_string, re.IGNORECASE)  # Игнорировать регистр
    filtered_transactions = [transaction for transaction in transactions if pattern.search(transaction['description'])]
    return filtered_transactions

def count_transaction_categories(transactions):
    """Подсчитывает количество банковских операций по описанию."""
    descriptions = [transaction['description'] for transaction in transactions]
    category_count = Counter(descriptions)
    return dict(category_count)