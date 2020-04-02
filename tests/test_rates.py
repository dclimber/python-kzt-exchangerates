import pytest
import datetime
import xml.etree.ElementTree as ET
from kzt_exchangerates import Rates


api = Rates()


# test internal methods
def test_get_latest_rss_url(latest_url):
    url = api._get_rss_url()
    assert url == latest_url


def test_get_dated_rss_url(date_for_tests, dated_url):
    url = api._get_rss_url(date_for_tests)
    assert url == dated_url


def test_fetch_rates_latest_rss(latest_url):
    res = api._fetch_rates(latest_url)
    assert (type(res)) == dict
    assert (res['rss'].__class__) == ET.Element
    assert (res['date'].__class__) == datetime.datetime


def test_fetch_rates_dated_rss(dated_url):
    res = api._fetch_rates(dated_url)
    assert (type(res)) == dict
    assert (res['rss'].__class__) == ET.Element
    assert (res['date'].__class__) == datetime.datetime


def test_parse_rates_from_rss(sample_rss):
    res = api._parse_rates_from_rss(sample_rss)
    assert (type(res)) == dict
    assert 'RUB' in res
    assert type(res['RUB']) == float


def test_get_supported_currencies(sample_rss, supported_currencies):
    supp = api._get_supported_currencies(sample_rss)
    assert supp == supported_currencies


def test_get_rates_for_targets(target_currencies, sample_rss):
    src_rates = api._parse_rates_from_rss(sample_rss)
    rates = api._get_rates_for_targets(False, target_currencies, src_rates)
    assert target_currencies == list(rates.keys())


# test public methods
def test_get_exchange_rates(supported_currencies):
    res = api.get_exchange_rates()
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    assert type(res) == dict
    assert 'rates' in res
    assert 'date' in res
    assert res['date'] == today
    assert len(res['rates']) >= len(supported_currencies)


def test_get_exchange_rates_dated(date_for_tests, result_date):
    res = api.get_exchange_rates(date=date_for_tests)
    assert res['date'] == result_date


def test_get_exchange_rates_for_targets(target_currencies):
    res = api.get_exchange_rates(target_currencies)
    assert target_currencies == list(res['rates'].keys())
    assert type(res['rates'][target_currencies[0]]) == float


def test_get_exchange_rates_from_kzt(supported_currencies):
    res = api.get_exchange_rates(from_kzt=True)
    assert res['rates']['USD'] > 100  # 1 USD is around 440 KZT


def test_get_exchange_rate():
    rate = api.get_exchange_rate('USD')
    assert rate < 1  # 1 KZT is around 0.00 of a US dollar


def test_get_exchange_rate_from_kzt():
    rate = api.get_exchange_rate('USD', from_kzt=True)
    assert rate > 100  # 1 USD is around 440 KZT


def test_get_exchange_rate_dated(date_for_tests):
    rate = api.get_exchange_rate('USD', from_kzt=True, date=date_for_tests)
    assert rate == 151.09  # from sample_rss.xml that is for the same date


def test_is_currency_supported():
    usd = api.is_currency_supported('USD')
    kkk = api.is_currency_supported('KKK')
    assert usd
    assert not kkk
