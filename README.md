# python-kzt-exchangerates
Simple python library for getting currency exchange rates from [National Bank of Republic of Kazakhstan rss feed](https://nationalbank.kz/rss/rates_all.xml).

The rss if free of charge, so you can ethically use it for your currency conversion operations.

Kazakhstan National Bank does not provide any API, so this library simply parses the data from their rss and then post-processes it for user's needs.

# Installation
Either clone this repository into your project, or install with `pip`:
```
pip install python-kzt-exchangerates
```

# Usage
```
from kzt_exchangerates import Rates

rates = Rates()

# Latest exchange rates for KZT (1 KZT = ...):
print(rates.get_exchange_rates())
{'rates':
{'AUD': 0.0038047407069208236, 'GBP': 0.0019146817798881828, 'DKK': 0.01567152483936687,
'AED': 0.008257638315441783, 'USD': 0.0022482014388489208, 'EUR': 0.0020974034145727592,
'CAD': 0.0031978510440983663, 'CNY': 0.01590583744234134, 'KWD': 0.0006994131923316338,
'KGS': 0.16339869281045752, 'LVL': 0.003322700691121744, 'MDL': 0.04024144869215292,
'NOK': 0.024443901246638967, 'SAR': 0.008449514152936207, 'RUB': 0.17482517482517484,
'XDR': 0.0016680567139282735, 'SGD': 0.003249074013906037, 'TRL': 10.0,
'UZS': 0.21413276231263384, 'UAH': 0.062460961898813235, 'SEK': 0.023062730627306273,
'CHF': 0.0022104332449160036, 'EEK': 0.08012820512820512, 'KRW': 0.027886224205242612,
'JPY': 0.24813895781637715, 'BYN': 0.005751754285056942, 'PLN': 0.009531071292413268,
'ZAR': 0.038880248833592534, 'TRY': 0.014613473622680109, 'HUF': 0.07342143906020558,
'CZK': 0.05652911249293386, 'TJS': 0.02190580503833516, 'HKD': 0.017439832577607253,
'BRL': 0.011456065986940083, 'MYR': 0.009869719699960523, 'AZN': 0.003787161522438932,
'INR': 0.16863406408094436, 'THB': 0.07315288953913679, 'AMD': 0.1107419712070875,
'GEL': 0.006897503103876397, 'IRR': 0.09433962264150944, 'MXN': 0.05350454788657035},
'date': '2020-03-26'}

# Latest exchange rates from KZT (... = ... KZT):
print(rates.get_exchange_rates(from_kzt=True))
{'rates': {'AUD': 262.83, 'GBP': 522.28, 'DKK': 63.81, 'AED': 121.1, 'USD': 444.8,
'EUR': 476.78, 'CAD': 312.71, 'CNY': 62.87, 'KWD': 1429.77, 'KGS': 6.12, 'LVL': 300.96,
'MDL': 24.85, 'NOK': 40.91, 'SAR': 118.35, 'RUB': 5.72, 'XDR': 599.5, 'SGD': 307.78,
'TRL': 0.1, 'UZS': 4.67, 'UAH': 16.01, 'SEK': 43.36, 'CHF': 452.4, 'EEK': 12.48,
'KRW': 35.86, 'JPY': 4.03, 'BYN': 173.86, 'PLN': 104.92, 'ZAR': 25.72, 'TRY': 68.43,
'HUF': 13.62, 'CZK': 17.69, 'TJS': 45.65, 'HKD': 57.34, 'BRL': 87.29, 'MYR': 101.32,
'AZN': 264.05, 'INR': 5.93, 'THB': 13.67, 'AMD': 9.03, 'GEL': 144.98, 'IRR': 10.6,
'MXN': 18.69}, 'date': '2020-03-26'}

# Exchange rates for KZT and USD, EUR, GBP for 12.01.2019 (1 KZT = ...):
print(rates.get_exchange_rates(["USD", "EUR", "GBP"], date="12.01.2019"))
{'rates': {'USD': 0.002659150135616657, 'EUR': 0.002308082906337996,
       'GBP': 0.0020852882911062453}, 'date': '12.01.2019'}

# Exchange rates for USD, EUR from KZT for 12.01.2019 (... = ... KZT):
print(rates.get_exchange_rates(["USD", "EUR"], from_kzt=True, date="12.01.2019"))
{'rates': {'USD': 376.06, 'EUR': 433.26}, 'date': '12.01.2019'}

# Currently 1 KZT ==
print(rates.get_exchange_rate("USD"))
0.0022482014388489208

# Currently 1 USD ==
print(rates.get_exchange_rate("USD", from_kzt=True))
444.8 KZT

# 1 GBP ==
print(rates.get_exchange_rate("GBP", from_kzt=True, date="12.01.2019"))
479.55

# 1 KZT ==
print(rates.get_exchange_rate("GBP", date="12.01.2019"))
0.0020852882911062453

# Get supported currencies:
print(rates.supported_currencies)
['AUD', 'GBP', 'DKK', 'AED', 'USD', 'EUR', 'CAD', 'CNY', 'KWD', 'KGS', 'LVL',
'MDL', 'NOK', 'SAR', 'RUB', 'XDR', 'SGD', 'TRL', 'UZS', 'UAH', 'SEK', 'CHF',
'EEK', 'KRW', 'JPY', 'BYN', 'PLN', 'ZAR', 'TRY', 'HUF', 'CZK', 'TJS', 'HKD',
'BRL', 'MYR', 'AZN', 'INR', 'THB', 'AMD', 'GEL', 'IRR', 'MXN', 'KZT']

# Is 'USD' currency supported:
print(rates.is_currency_supported("USD"))
True

# Is 'KKK' currency supported:
print(rates.is_currency_supported("KKK"))
False

```

# Version 0.1.0 update:
It was possible to get rates for any supported currency, by calculating the rate through KZT.
For example USD to KZT = {usd_rate}, GBP to KZT = {gbp_rate}, so it was producing USD to GBP
rate by {usd_rate}/{gbp_rate}, which is correct math, but Economy does not work that way!

So now such methods are removed, because wrong rates were produced.

Now it is only possible to get exchange rate from Kazakhstani Tenge or to Kazakhstani Tenge.

I've realised it, when Kazakhstani Tenge devaluated from 1 USD = 390 KZT to 1 USD = 440 KZT
in March 2020. Russian Ruble has dropped even lower, so proper exchange rate for
Kazakhstani Tenge was around 1 USD = 480 KZT... but it was not the case, because
Kazakhstan's National Bank was 'holding' Tenge from dropping to its real value.

# Supported currencies
The list of currencies provided by [Kazakhstan National Bank's rss feed](https://nationalbank.kz/rss/rates_all.xml):
```
AUD - Australia Dollar
GBP - United Kingdom Pound
DKK - Denmark Krone
AED - United Arab Emirates Dirham
USD - United States Dollar
EUR - Euro Member Countries
CAD - Canada Dollar
CNY - China Yuan Renminbi
KWD - Kuwait Dinar
KGS - Kyrgyzstan Som
LVL - Latvian Lat
MDL - Moldova Leu
NOK - Norway Krone
SAR - Saudi Arabia Riyal
RUB - Russia Ruble
XDR - International Monetary Fund (IMF) Special Drawing Rights
SGD - Singapore Dollar
TRL - Turkish Lira
UZS - Uzbekistan Som
UAH - Ukraine Hryvnia
SEK - Sweden Krona
CHF - Switzerland Franc
EEK - Estonian Kroon
KRW - South Korean Won
KZT - Kazakhstan Tenge
JPY - Japan Yen
BYN - Belarus Ruble
PLN - Poland Zloty
ZAR - South Africa Rand
TRY - Turkey Lira
HUF - Hungary Forint
CZK - Czech Republic Koruna
TJS - Tajikistan Somoni
HKD - Hong Kong Dollar
BRL - Brazil Real
MYR - Malaysia Ringgit
AZN - Azerbaijan Manat
INR - India Rupee
THB - Thailand Baht
AMD - Armenia Dram
GEL - Georgia Lari
IRR - Iran Rial
MXN - Mexico Peso
```
If your currency is not in the list, then the library will be of not use to you. You may try [openexchangerates.org API](https://github.com/metglobal/openexchangerates) or some other service.
# License
MIT