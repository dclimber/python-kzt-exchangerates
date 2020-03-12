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

print('Latest exchange rates for KZT:\n%s' % rates.get_exchange_rates())
print('\nLatest exchange rates for USD:\n%s' % rates.get_exchange_rates('USD'))
print(
    '\nExchange rates for RUB on 12.01.2019:\n%s' %
    rates.get_exchange_rates('RUB', date="12.01.2019")
)
print(
    '\nExchange rates for USD and KZT,EUR,GBP for 12.01.2019:\n%s' %
    rates.get_exchange_rates('USD', ['KZT', 'EUR', 'GBP'], date='12.01.2019')
)
print(
    '\nCurrent exchange rates for USD and required currencies:\n%s' %
    rates.get_exchange_rates('USD', ['CAD', 'EUR', 'GBP', 'AUD', 'RUB'])
)
print('\nCurrently 1 KZT = %s %s' %
      (rates.get_exchange_rate('KZT', 'USD'), 'USD'))
print('\nCurrently 1 USD = %s %s' %
      (rates.get_exchange_rate('USD', 'KZT'), 'KZT'))
print('\n1 KZT = %s %s' %
      (rates.get_exchange_rate('KZT', 'USD', '12.01.2019'), 'USD on 12.01.2019'))
print('\n1 EUR = %s %s' %
      (rates.get_exchange_rate('EUR', 'RUB', '12.01.2007'), 'RUB on 12.01.2019'))

```
This will output:
```
Latest exchange rates for KZT:
{'rates': {'AUD': 0.0038850038850038854, 'GBP': 0.001955569461827284,
'DKK': 0.01675041876046901, 'AED': 0.009307520476545048, 'USD': 0.002534211860111505,
'EUR': 0.0022420519259226043, 'CAD': 0.0034711374917560486, 'CNY': 0.017614937466971993,
'KWD': 0.0007764819157361826, 'KGS': 0.17699115044247787, 'LVL': 0.003322700691121744,
'MDL': 0.04409171075837742, 'NOK': 0.0243605359317905, 'SAR': 0.009511128019783146,
'RUB': 0.1811594202898551, 'XDR': 0.0018183140592043056, 'SGD': 0.0035226151895166972,
'TRL': 10.0, 'UZS': 0.24096385542168672, 'UAH': 0.0649772579597141, 'SEK': 0.024078979051288224,
'CHF': 0.0023745636739249164, 'EEK': 0.08012820512820512, 'KRW': 0.030184123151222455,
'JPY': 0.26595744680851063, 'BYN': 0.005860290670417253, 'PLN': 0.009672115291614276,
'ZAR': 0.0407000407000407, 'TRY': 0.015634771732332707, 'HUF': 0.07501875468867217,
'CZK': 0.0574712643678161, 'TJS': 0.024521824423737126, 'HKD': 0.019688915140775743,
'BRL': 0.011764705882352941, 'MYR': 0.010719262514738986, 'AZN': 0.004290372404324695,
'INR': 0.1869158878504673, 'THB': 0.07961783439490445, 'AMD': 0.12195121951219513,
'GEL': 0.00702000702000702, 'IRR': 0.10638297872340426, 'MXN': 0.05319148936170213},
'base_currency': 'KZT', 'date': '2020-03-12'}

Latest exchange rates for USD:
{'rates': {'AUD': 1.5330225330225333, 'GBP': 0.7716677096370463, 'DKK': 6.609715242881072,
'AED': 3.6727475800446765, 'EUR': 0.8847136899690597, 'CAD': 1.369710854246937,
'CNY': 6.950854324467148, 'KWD': 0.30639976394949764, 'KGS': 69.84070796460178, 'LVL': 1.3111376927166403, 'MDL': 17.398589065255734, 'NOK': 9.612667478684532, 'SAR': 3.75309111660643,
'RUB': 71.48550724637683, 'XDR': 0.7175067277620191, 'SGD': 1.3900239537832888, 'TRL': 3946.0,
'UZS': 95.08433734939759, 'UAH': 25.640025990903183, 'SEK': 9.501565133638334, 'CHF': 0.937002825730772, 'EEK': 31.618589743589745, 'KRW': 11.910654995472381, 'JPY': 104.9468085106383,
'BYN': 2.3124706985466483, 'PLN': 3.8166166940709934, 'ZAR': 16.06023606023606,
'TRY': 6.169480925578487, 'HUF': 29.602400600150037, 'CZK': 22.678160919540232,
'TJS': 9.67631191760667, 'HKD': 7.769245914550109, 'BRL': 4.642352941176471,
'MYR': 4.229820988316003, 'AZN': 1.6929809507465248, 'INR': 73.7570093457944, 
'THB': 31.4171974522293, 'AMD': 48.121951219512205, 'GEL': 2.7700947700947705, 
'IRR': 41.97872340425532, 'MXN': 20.98936170212766, 'KZT': 394.6},
'base_currency': 'USD', 'date': '2020-03-12'}

Exchange rates for RUB on 12.01.2019:
{'rates': {'AUD': 0.020710495283018868, 'AZN': 0.025300499707378563, 'AMD': 0.7242268041237113,
'BYN': 0.032130810130924475, 'BRL': 0.05545140601874692, 'HUF': 0.41660489251297256,
'HKD': 0.11718098415346122, 'GEL': 0.039633286318758815, 'DKK': 0.09681309216192938,
'AED': 0.054888172673112606, 'USD': 0.014944423762165612, 'EUR': 0.012971425933619536,
'INR': 1.0544090056285178, 'IRR': 0.6244444444444445, 'CAD': 0.019708925127126076,
'CNY': 0.1007168458781362, 'KWD': 0.004524559016512226, 'KGS': 1.0407407407407407,
'MYR': 0.06118005660788156, 'MXN': 0.28513444951801115, 'MDL': 0.25406871609403253,
'NOK': 0.12637733303350573, 'PLN': 0.05571527708932289, 'SAR': 0.05605425892679034,
'XDR': 0.01069152477884524, 'SGD': 0.020185331513540693, 'TJS': 0.14092276830491474,
'THB': 0.47667514843087366, 'TRY': 0.08120213841930357, 'UZS': 1.246119733924612,
'UAH': 0.4200298953662182, 'GBP': 0.011719320196017098, 'CZK': 0.3317591499409681,
'SEK': 0.13273500236183278, 'CHF': 0.014685899446012333, 'ZAR': 0.20639001101726037,
'KRW': 0.16656787196206282, 'JPY': 1.6195965417867435, 'KZT': 5.62},
'base_currency': 'RUB', 'date': '12.01.2019'}

Exchange rates for USD and KZT,EUR,GBP for 12.01.2019:
{'rates': {'KZT': 376.06, 'EUR': 0.8679776577574667, 'GBP': 0.7841935147534147},
'base_currency': 'USD', 'date': '12.01.2019'}

Current exchange rates for USD and required currencies:
{'rates': {'CAD': 1.369710854246937, 'EUR': 0.8847136899690597, 'GBP': 0.7716677096370463,
'AUD': 1.5330225330225333, 'RUB': 71.48550724637683}, 'base_currency': 'USD',
'date': '2020-03-12'}

Currently 1 KZT = 0.002534211860111505 USD

Currently 1 USD = 394.6 KZT

1 KZT = 0.002659150135616657 USD on 12.01.2019

1 EUR = 34.401691331923885 RUB on 12.01.2019
```

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