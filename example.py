from kzt_exchangerates import Rates

rates = Rates()

print('Latest exchange rates for KZT (1 KZT = ...):\n%s' %
      rates.get_exchange_rates())
print('\nLatest exchange rates from KZT (... = ... KZT):\n%s' %
      rates.get_exchange_rates(from_kzt=True))
print(
  '\nExchange rates for KZT and USD, EUR, GBP for 12.01.2019 (1 KZT = ...):\n%s' %
  rates.get_exchange_rates(['USD', 'EUR', 'GBP'], date='12.01.2019')
)
print(
  '\nExchange rates for USD, EUR from KZT for 12.01.2019 (... = ... KZT):\n%s' %
  rates.get_exchange_rates(['USD', 'EUR'], from_kzt=True, date='12.01.2019')
)
print('\nCurrently 1 KZT = %s %s' %
      (rates.get_exchange_rate('USD'), 'USD'))
print('\nCurrently 1 USD = %s %s' %
      (rates.get_exchange_rate('USD', from_kzt=True), 'KZT'))
print('\n1 GBP = %s %s' %
      (rates.get_exchange_rate('GBP', from_kzt=True, date='12.01.2019'),
       'KZT on 12.01.2019'))
print('\n1 KZT = %s %s' %
      (rates.get_exchange_rate('GBP', date='12.01.2019'), 'GBP on 12.01.2019'))
