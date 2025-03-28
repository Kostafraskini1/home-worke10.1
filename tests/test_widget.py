import pytest
from src.widget import mask_account_card

@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Account 123456789012", "Account **9012"),
    ("Invalid Data", "Invalid Data "),
    ("", " "),
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected





