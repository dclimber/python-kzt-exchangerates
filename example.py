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
