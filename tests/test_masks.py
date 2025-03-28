import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number("") == ""

def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account("98765432") == "**5432"
    assert get_mask_account("") == ""

