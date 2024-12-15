import pytest

from src.masks import get_mask_account, get_mask_card_number





@pytest.mark.parametrize("numbers, masks", [("7000792289606361", "7000 79** **** 6361"),
                                            ("4571354875129009", "4571 35** **** 9009"),
                                            ("2504786942057145", "2504 78** **** 7145")])


def test_get_mask_card_number(card_number_int=None, card_number_str=None) -> None:
    """Тестирование правильности маскирования номера карты в формате числа и строки
    :param card_number_srt:
    :param card_number_int:
    """
    assert get_mask_card_number(card_number_srt) == "7000 79** **** 6361"
    assert get_mask_card_number(card_number_int) == "7000 79** **** 6361"

def test_get_mask_card_number_letter() -> None:
    """Тест на обработку ошибки ввода номера карты, в случае ввода посторонних символов"""
    assert get_mask_card_number("700079в89606361") == "Не верный формат номера карты"
    assert get_mask_card_number("70@0792=9606361") == "Не верный формат номера карты"


def test_get_mask_card_number_long(card_number_int: int, card_number_str: str) -> None:
    """Тест на обработку неверной длины номера карты"""
    assert get_mask_card_number(card_number_int) == "Не верный формат номера карты"
    assert get_mask_card_number(card_number_str) == "Не верный формат номера карты"

def test_get_mask_card_number_empty(empty_value: str) -> None:
    """Тест на обработку ошибки, при пустом значении номера карты"""
    assert get_mask_card_number(empty_value) == "Не верный формат номера карты"


def test_get_mask_account(account_number_int: int, account_number_str: str) -> None:
    """Тестирование правильности маскирования номера счета в формате числа и строки"""
    assert get_mask_account(account_number_int) == "**4305"
    assert get_mask_account(account_number_str) == "**4305"


def test_get_mask_account_letter() -> None:
    """Тестирование правильности маскирования номера счета в формате числа и строки"""
    assert get_mask_account("736541084k013j874305") == "Не верный формат номера счета"
    assert get_mask_account("736541084@013=874305") == "Не верный формат номера счета"


def test_get_mask_account_long(account_number_int: int, account_number_str: str) -> None:
    """Тест на обработку неверной длины номера счета"""
    assert get_mask_account(account_number_int) == "Не верный формат номера счета"
    assert get_mask_account(account_number_str) == "Не верный формат номера счета"


def test_get_mask_account_empty(empty_value: str) -> None:
    """Тест на обработку ошибки, при пустом значении номера счета"""
    assert get_mask_account(empty_value) == "Не верный формат номера карты"





