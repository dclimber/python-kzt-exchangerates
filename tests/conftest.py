import pytest
from pathlib import Path
import xml.etree.ElementTree as ET


@pytest.fixture
def date_for_tests():
    return '24.04.2013'


@pytest.fixture
def result_date():
    return '2013-04-24'


@pytest.fixture
def latest_url():
    return 'https://nationalbank.kz/rss/rates_all.xml'


@pytest.fixture
def dated_url(date_for_tests):
    return 'https://nationalbank.kz/rss/get_rates.cfm?fdate={}'.format(
                                                                date_for_tests)


@pytest.fixture
def sample_rss():
    # rss file for 2013-04-24 (date for tests)
    file = Path("sample_rss.xml")
    text = file.read_text()
    rss = ET.fromstring(text)
    return rss


@pytest.fixture
def supported_currencies():
    # currencies from sample_rss.xml
    return ['AUD', 'GBP', 'BYR', 'BRL', 'HUF', 'HKD', 'DKK', 'AED', 'USD',
            'EUR', 'CAD', 'CNY', 'KWD', 'KGS', 'LVL', 'LTL', 'MYR', 'MDL',
            'NOK', 'PLN', 'SAR', 'RUB', 'XDR', 'SGD', 'TJS', 'TRY', 'UZS',
            'UAH', 'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY', 'KZT']


@pytest.fixture
def target_currencies():
    return ['AUD', 'GBP', 'DKK', 'AED', 'USD', 'EUR', 'CAD', 'CNY', 'KWD']
