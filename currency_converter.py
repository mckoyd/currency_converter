import json
import requests
import sys

from config import access_key
from decimal import Decimal, ROUND_HALF_UP

class Currency(object):
    def __init__(self, resource_name):
        self.base_url = 'http://www.apilayer.net/api/'
        self.resources = {
            'live': 'live?access_key={}',
            'list': 'list?access_key={}',
        }
        self.full_url = (self.base_url + self.resources[resource_name]).format(access_key)
        self.response = None
    
    def get_data(self):
        r = requests.get(self.full_url)
        if r.status_code > 299:
            print("Your request to the site '{}' failed with a {} error.").format(r.url, r.status_code)
            return
        else:
            self.response = r.json()
            return self.response

CURRENCY_RATES = Currency('live').get_data()['quotes']
CURRENCY_ABBREVIATIONS = Currency('list').get_data()['currencies']

def get_abbr(currency_name):
  for abbr in CURRENCY_ABBREVIATIONS:
    if(currency_name == CURRENCY_ABBREVIATIONS[abbr]):
      return f'USD{abbr}'

def get_currency_rate(currency_name):
  for rate in CURRENCY_RATES:
    if(get_abbr(currency_name) == rate):
      return CURRENCY_RATES[rate]

def convert_from_US(name, amount):
  rate = get_currency_rate(name)
  return Decimal(amount * rate).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

def convert_to_US(name, amount):
  rate = get_currency_rate(name)
  return Decimal(amount / rate).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

print(convert_to_US('Euro', 5000))  

# print(json.dumps(CURRENCY_RATES, indent=2))
# print(currencyList['quotes']['USDEUR'])