import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

def test_filter_by_state(sample_data):
    assert filter_by_state(sample_data, 'EXECUTED') == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    assert filter_by_state(sample_data, 'CANCELED') == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    assert filter_by_state(sample_data, 'NON_EXISTENT') == []

@pytest.mark.parametrize("type_sort, expected_order", [
    (True, [41428829, 939719570, 594226727, 615064591]),
    (False, [615064591, 594226727, 939719570, 41428829]),
])
def test_sort_by_date(sample_data, type_sort, expected_order):
    sorted_data = sort_by_date(sample_data, type_sort)
    assert [item['id'] for item in sorted_data] == expected_order
