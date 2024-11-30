import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


def test_mask_account_card_card() -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == "7000 79** **** 6361"

def test_mask_account_card_account() -> None:
    assert mask_account_card("Счет 73654108430135874305") == "**4305"


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "7158 30** **** 6758"),
        ("Счет 35383033474447895560", "**5560")
        ]
)


def test_mask_account_card_diff(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected


@pytest.mark.parametrize(
    "number", ("Visa 456789", "1234567897898778", "Счет 77778845", "fghjkjklh")
)


def test_mask_account_card_invalid(number: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(number)


@pytest.mark.parametrize("date_string, expected_output", [
    ("2023-10-10", "2023-10-10"),
    ("10/10/2023", "2023-10-10"),
    ("01-01-2020", "2020-01-01"),
    ("", None),
    ("invalid-date", None)
])
def test_get_data(date_strings, expected_output):
    for date_string in date_strings:
        result = get_date(date_string)
        assert result == expected_output





