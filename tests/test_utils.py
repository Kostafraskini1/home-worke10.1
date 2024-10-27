import unittest
from unittest.mock import patch, mock_open
from utils import load_transactions


class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "RUB"}]')
    def test_load_transactions_success(self, mock_file):
        result = load_transactions('dummy_path')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['amount'], 100)

    @patch("os.path.exists", return_value=False)
    def test_load_transactions_file_not_found(self, mock_exists):
        result = load_transactions('dummy_path')
        self.assertEqual(result, [])
        