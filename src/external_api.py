import os
from locale import currency

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def convert_to_rub(transaction):
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if transaction['currency'] == 'RUB':
        return float(transaction['amount'])

    response = requests.get(
        f'https://api.apilayer.com/exchangerates_data/convert?to={transaction["currency"]}&symbols=RUB',
        headers={'apikey': API_KEY}
    )
    response.raise_for_status()
    result = response.json()

    return float(transaction['amount']) * result['result']['RUB']



