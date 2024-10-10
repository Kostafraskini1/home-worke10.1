import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(data_list):
    result = filter_by_state(data_list, "active")
    expected = [
        {"state": "active", "date": "2023-10-01"},
        {"state": "active", "date": "2023-08-01"}
    ]
    assert result == expected


@pytest.mark.parametrize("state, expected", [
    ("inactive", [{"state": "inactive", "date": "2023-09-01"}]),
    ("pending", [{"state": "pending", "date": "2023-10-05"}]),
    ("active", [
        {"state": "active", "date": "2023-10-01"},
        {"state": "active", "date": "2023-08-01"}
    ]),
])
def test_filter_by_state_parametrized(data_list, state, expected):
    result = filter_by_state(data_list, state)
    assert result == expected


def test_sort_by_date(data_list):
    result = sort_by_date(data_list)
    expected = [
        {"state": "active", "date": "2023-10-01"},
        {"state": "pending", "date": "2023-10-05"},
        {"state": "inactive", "date": "2023-09-01"},
        {"state": "active", "date": "2023-08-01"}
    ]
    assert result == expected
