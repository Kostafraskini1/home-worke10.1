
import logging
import os.path
from fileinput import filename
from venv import logger


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..//logs//masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    logger.info(f"Маскирует номер карты клиента")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    logger.info(f"Маскирует номер счета клиента")
    return f"**{account_number[-4:]}"



