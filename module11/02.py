# import json

# dump -> serialize into file
# dumps -> serialize into var of type str
# load -> deserialize back to obj from the file
# loads -> deserialize back to obj from the var

# d = {"age": 1}

# #json - js notation object = dictionaries

# d_str = json.dumps(d)
# print(type(d_str))
# print(d_str)


from datetime import date, timedelta
import requests
from pprint import pprint
import json

API_URL = "https://api.privatbank.ua/p24api/exchange_rates?date={d}"

currencies = ("USD", "EUR")


def get_exchange_rate(date):
    response = requests.get(API_URL.format(d=date))
    response.raise_for_status()
    data = response.json()
    rates = list(
        filter(lambda x: x.get("currency") in currencies, data.get("exchangeRate"))
    )
    data["exchangeRate"] = rates
    return data


def get_rates_delta(since):
    results = []
    days = (date.today() - since).days + 1
    for i in range(days):
        d = since + timedelta(i)
        d_str = d.strftime("%d.%m.%Y")
        results.append(get_exchange_rate(d_str))
    return results
    # print(json.dumps(results, indent=4))


since = date(2025, 7, 1)
rates = get_rates_delta(since)

with open("rates.json", "w") as f:
    json.dump(rates, f, sort_keys=True, indent=4)
