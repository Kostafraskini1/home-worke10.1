
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