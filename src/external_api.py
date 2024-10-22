import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def convert_to_rub(transaction):
    if transaction['currency'] == 'RUB':
        return float(transaction['amount'])

    response = requests.get(
        f'https://api.apilayer.com/exchangerates_data/latest?base={transaction["currency"]}&symbols=RUB',
        headers={'apikey': API_KEY}
    )
    response.raise_for_status()
    rates = response.json()

    return float(transaction['amount']) * rates['rates']['RUB']
