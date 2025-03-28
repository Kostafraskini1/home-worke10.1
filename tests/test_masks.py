import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("", ""),
    ("1234", "1234"),
    ("12345678901234567890", "1234 56** **** 3456"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number, expected", [
    ("123456789012", "**9012"),
    ("1234", "**34"),
    ("", ""),
    ("123456", "**56"),
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

