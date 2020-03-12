# python-kzt-exchangerates
Simple python library for getting currency exchange rates from [National Bank of Republic of Kazakhstan rss feed](https://nationalbank.kz/rss/rates_all.xml).

The rss if free of charge, so you can ethically use it for your currency conversion operations.

Kazakhstan National Bank does not provide any API, so this library simply parses the data from their rss and then post-processes it for user's needs.

# Supported currencies
The list of currencies provided by [Kazakhstan National Bank's rss feed](https://nationalbank.kz/rss/rates_all.xml):
```
AUD, GBP, DKK, AED, USD, EUR, CAD, CNY, KWD, KGS, LVL,
MDL, NOK, SAR, RUB, XDR, SGD, TRL, UZS, UAH, SEK, CHF,
EEK, KRW, JPY, BYN, PLN, ZAR, TRY, HUF, CZK, TJS, HKD,
BRL, MYR, AZN, INR, THB, AMD, GEL, IRR, MXN, KZT
```
If your currency is not in the list, then the library will be of not use to you. You may try [openexchangerates.org API](https://github.com/metglobal/openexchangerates) or some other service.
# License
MIT