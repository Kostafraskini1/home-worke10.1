import unittest
from unittest.mock import patch
from external_api import convert_to_rub


class TestExternalAPI(unittest.TestCase):

    @patch('requests.get')
    def test_convert_to_rub(self, mock_get):
        mock_get.return_value.json.return_value = {'rates': {'RUB': 75}, 'success': True}
        mock_get.return_value.raise_for_status = lambda: None

        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)

        transaction['currency'] = 'RUB'
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)


if __name__ == '__main__':
    unittest.main()
