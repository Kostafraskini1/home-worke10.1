import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 12345678901234567890") == "Счет **7890"
    assert mask_account_card("Некорректные данные") == "Некорректные данные "
    assert mask_account_card("Текст без номеров") == "Текст без номеров "

def test_get_date():
    assert get_date("2021-10-13") == "13.10.2021"
    assert get_date("2023-01-01") == "01.01.2023"
    assert get_date("Неизвестная дата") == "Неизвестная дата"






