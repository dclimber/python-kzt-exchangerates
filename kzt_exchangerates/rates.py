import requests
import datetime
import xml.etree.ElementTree as ET


class Rates(object):
    LATEST = 'latest'
    DATE = 'date'
    KZT_CODE = 'KZT'
    rss_url = 'https://nationalbank.kz/rss/{endpoint}'
    rss_endpoints = {
        LATEST: 'rates_all.xml',
        DATE: 'get_rates.cfm?fdate={date}'  # in dd.mm.YYYY format
    }
    latest_rates = None

    def __init__(self):
        """Initialize the object by fetching latest rates."""
        latest_url = self._get_rss_url()
        self.latest_rates = self._fetch_rates(latest_url)

    def _fetch_rates(self, url, date=None):
        """Method for fetching currency rates from Kazakhstan National
        Bank's rss feed, using provided url.

        If self.latest_rates exists, returns self.latest_rates.
        Otherwise fetches data from Bank's rss feed.

        Args:
            param1 (obj): self
            param2 (str): rss url

        Returns:
            {
                'rss': parsed ElementTree xml tree,
                'date': datetime.datetime object
            }
        """
        if self.latest_rates and not date:
            return self.latest_rates
        # not 'cached' rates -> fetch them
        response = requests.get(url)
        rss = ET.fromstring(response.text)
        date = datetime.datetime.strptime(
            response.headers['date'], '%a, %d %b %Y %H:%M:%S %Z')
        return {'rss': rss, 'date': date}

    def _parse_rates_from_rss(self, rss):
        """Method for parsing provided rss feed.

        Args:
            param1 (obj): self
            param2 (obj): ElementTree xml tree

        Returns:
            dict: {str(currency code): float(exchange rate), ...}
        """
        rates = dict([
            (item.find('title').text,
                float(item.find('description').text))
            for item in rss.iter('item')
            ])
        # add KZT
        rates[self.KZT_CODE] = 1
        return rates

    def _get_rss_url(self, date=None):
        """Method for getting correct rss url.

        Args:
            param1 (obj): self
            param2 (str): date

        Returns:
            str: url
        """
        if date:
            return self.rss_url.format(
                endpoint=self.rss_endpoints[self.DATE].format(date=date))
        return self.rss_url.format(
                endpoint=self.rss_endpoints[self.LATEST])

    def _calculate_through_kzt(self, base, target, rates):
        """Method to calculate exchange rate through exchange
        rates for Kazakhstani Tenge.

        Args:
            param1 (obj): self
            param2 (str): base currency
            param3 (str): target currency
            param4 (dict): KZT exchange rates dictionary

        Returns:
            float()
        """
        if target == self.KZT_CODE:
            return rates[base]
        elif base == self.KZT_CODE:
            return rates[target]
        else:
            base_to_med = rates[base]
            target_to_med = rates[target]
            return base_to_med / target_to_med

    def _get_rates_for_currency(self, base, target_list, rates):
        """Method for getting exchange rates for given currency
        based on Kazakhstani Tenge exchange rates.

        Args:
            param1 (obj): self
            param2 (str): base currency
            param3 [str]: target currency list
            param4 (dict): KZT exchange rates dictionary

        Returns:
            A dicionary with currency rates for the provided currency.

            {
                str(currency code): float(exchange rate), ...
            }
        """
        if not target_list:
            target_list = [cur for cur in rates if cur != base]
        if base == self.KZT_CODE:
            return dict([(targ, 1 / rates[targ]) for targ in target_list])
        return dict(
                [(targ, self._calculate_through_kzt(
                    base, targ, rates)) for targ in target_list])

    def get_exchange_rates(self, base='KZT', currency_list=[], date=None):
        """Method for gettings currency exchange rates for
        Kazakhstani Tenge, KZT.

        Args:
            param1 (obj): self
            param2 (str): date string in format dd.mm.YYYY
            param3 (str): 3-letter currency code
            param4 (list): list of 3-letter currency code strings

        Returns:
            A dicionary with currency rates for the provided currency,
            for the provided date or for the current moment, if no
            date was provided.

            {
                'rates': {str(currency code): float(exchange rate), ...},
                'base_currency': 'KZT',
                'date': YYYY-mm-dd,
            }

        Examples:
            >>> api.get_exchange_rates()
            {'rates': {'AUD': 257.11, GBP: 511.29 ...}, base_currency: 'KZT',
            'date': '2020-03-12'}
            >>> api.get_exchange_rates(date='12.01.2019', base_currency='USD',
                    currency_list=['KZT', 'EUR', 'GBP'])
            {'rates': {'KZT': 393.4, 'EUR': 1.12, 'GBP': 1.56},
             'base_currency': 'USD', 'date': '2019-01-12'}
        """
        url = self._get_rss_url(date)
        fetched_data = self._fetch_rates(url, date)
        rates = self._parse_rates_from_rss(fetched_data['rss'])
        if date:
            res_date = fetched_data['rss'].find('date').text
        else:
            res_date = fetched_data['date'].strftime('%Y-%m-%d')
        res_rates = self._get_rates_for_currency(
            base, currency_list, rates)
        return {'rates': res_rates, 'base_currency': base,
                'date': res_date}

    def get_exchange_rate(self, base, target, date=None):
        """Method to get exchange rate for a given currency
        for a given date.

        Args:
            param1 (obj): self
            param2 (str): date string in format dd.mm.YYYY
            param3 (str): 3-letter currency code
            param4 (str): 3-letter currency code

        Returns:
            (float): currency rate

        Examples:
            >>> api.get_exchange_rate()
            394.55
            >>> api.get_exchange_rate(date='12.01.2019',
                                       base_currency='USD', target='EUR')
            0.897
        """
        res = self.get_exchange_rates(date=date,
                                      base=base,
                                      currency_list=[target])
        return res['rates'][target]
