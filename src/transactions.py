import re
from collections import Counter

def filter_transactions(transactions, search_string):
    """Фильтрует список транзакций по строке поиска в описании с использованием регулярных выражений."""
    pattern = re.compile(search_string, re.IGNORECASE)  # Игнорировать регистр
    filtered_transactions = [transaction for transaction in transactions if pattern.search(transaction['description'])]
    return filtered_transactions

def count_transaction_categories(transactions, categories):
    """Подсчитывает количество банковских операций по указанным категориям."""
    # Инициализируем словарь для подсчёта
    category_count = {category: 0 for category in categories}

    # Подсчитываем количество операций для каждой категории
    for transaction in transactions:
        description = transaction['description']
        # Проверяем, относится ли описание к какой-либо из категорий
        for category in categories:
            if category in description:
                category_count[category] += 1

    return category_count