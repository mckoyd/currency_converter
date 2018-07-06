import requests
import sys
from config import access_key
from decimal import Decimal, ROUND_HALF_UP

class Currency(object):
    def __init__(self, resource_name, source):
        self.base_url = 'http://www.apilayer.net/api/'
        self.resources = {
            'live': 'live?access_key={}&source={}',
            'list': 'list?access_key={}&source={}',
        }
        self.full_url = (self.base_url + self.resources[resource_name]).format(access_key, source)
        self.response = None
    
    def get_data(self):
        r = requests.get(self.full_url)
        if r.status_code > 299:
            print("Your request to the site '{}' failed with a {} error.").format(r.url, r.status_code)
            return
        else:
            self.response = r.json()
            return self.response


def get_abbr(source, currency_name):
  CURRENCY_ABBREVIATIONS = Currency('list', source).get_data()['currencies']
  for abbr in CURRENCY_ABBREVIATIONS:
    if(currency_name == CURRENCY_ABBREVIATIONS[abbr]):
      return f'{source}{abbr}'

def get_currency_rate(source, currency_name):
  CURRENCY_RATES = Currency('live', source).get_data()['quotes']
  if (len(currency_name) > 3 ):
    for rate in CURRENCY_RATES:
      if(get_abbr(source, currency_name) == rate):
        return CURRENCY_RATES[rate]
  else:
    for rate in CURRENCY_RATES:
      if(f'{source}{currency_name}' == rate):
        return CURRENCY_RATES[rate]

def convert_to_source(source, currency_name, currency_amount):
  rate = get_currency_rate(source, currency_name)
  return Decimal(currency_amount * rate).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

def convert_from_source(source, currency_name, currency_amount):
  rate = get_currency_rate(source, currency_name)
  return Decimal(currency_amount / rate).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)