import json
import os
import datetime
import logging
from fileinput import filename
from venv import logger


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..//logs//utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

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
