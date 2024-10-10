import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("numbers, masks", [("7000792289606361", "7000 79** **** 6361"),
                                            ("4571354875129009", "4571 35** **** 9009"),
                                            ("2504786942057145", "2504 78** **** 7145")])

def test_get_mask_card_number(numbers, masks):
    assert numbers == masks


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
