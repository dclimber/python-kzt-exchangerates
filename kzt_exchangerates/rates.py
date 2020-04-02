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
    supported_currencies = None

    def __init__(self):
        """Initialize the object by fetching latest rates
        and getting supported currencies.
        """
        latest_url = self._get_rss_url()
        self.latest_rates = self._fetch_rates(latest_url)
        self.supported_currencies = self._get_supported_currencies(
            self.latest_rates['rss']
        )

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

    def _get_supported_currencies(self, rss_feed):
        """Returns a list of supported currencies."""
        return [cur for cur in self._parse_rates_from_rss(rss_feed)]

    def _get_rates_for_targets(self, from_kzt, target_list, rates):
        """Method for getting exchange rates for given currencies
        based on Kazakhstani Tenge exchange rates.

        Args:
            param1 (obj): self
            param2 (bool): calculate from KZT?
            param3 [str]: target currency list
            param4 (dict): KZT exchange rates dictionary

        Returns:
            A dicionary with currency rates for or from Kazakhstani Tenge.

            {
                str(currency code): float(exchange rate), ...
            }
        """
        if not target_list:
            target_list = [cur for cur in rates if cur != self.KZT_CODE]
        if not from_kzt:
            return dict([(targ, 1 / rates[targ]) for targ in target_list])
        return dict([(targ, rates[targ]) for targ in target_list])

    def get_exchange_rates(self, targets=[], from_kzt=False, date=None):
        """Method for gettings currency exchange rates for or from
        Kazakhstani Tenge.

        Args:
            param1 (obj): self
            param2 (list): list of 3-letter currency code strings
            param3 (bool): calculate from KZT?
            param4 (str):  string in format dd.mm.YYYY

        Returns:
            A dicionary with currency rates for or from Kazakhstani Tenge,
            for the provided date or for the current moment, if no
            date was provided.

            {
                'rates': {str(currency code): float(exchange rate), ...},
                'date': YYYY-mm-dd,
            }

        Examples:
            >>> rates.get_exchange_rates()
            {'rates': {'AUD': 0.0038047407069208236,
                       'GBP': 0.0019146817798881828, ...},
             'date': '2020-03-26'}
            >>> rates.get_exchange_rates(from_kzt=True)
            {'rates': {'AUD': 262.83, 'GBP': 522.28, ...},
             'date': '2020-03-26'}
        """
        # fetch data / get cached data
        url = self._get_rss_url(date)
        fetched_data = self._fetch_rates(url, date)
        rates = self._parse_rates_from_rss(fetched_data['rss'])
        if date:
            # date in format: dd.mm.YYYY
            fetched_date = fetched_data['rss'].find('date').text
            fd_list = fetched_date.split('.')
            res_date = "{}-{}-{}".format(fd_list[2], fd_list[1], fd_list[0])
        else:
            res_date = fetched_data['date'].strftime('%Y-%m-%d')
        # get rates
        res_rates = self._get_rates_for_targets(from_kzt, targets, rates)
        return {'rates': res_rates, 'date': res_date}

    def get_exchange_rate(self, target, from_kzt=False, date=None):
        """Method to get exchange rate for or from Kazakhstani Tenge.

        Args:
            param1 (obj): self
            param2 (str): 3-letter currency code
            param3 (str): calculate from KZT?
            param4 (str): date string in format dd.mm.YYYY

        Returns:
            (float): currency rate

        Examples:
            >>> api.get_exchange_rate('USD')
            0.0022482014388489208
            >>> api.get_exchange_rate('USD', from_kzt=True)
            444.8
            >>> api.get_exchange_rate('USD', from_kzt=True, date='12.01.2019')
            380.44
        """
        res = self.get_exchange_rates(date=date, from_kzt=from_kzt,
                                      targets=[target])
        return res['rates'][target]

    def is_currency_supported(self, currency):
        """Returns True or False."""
        return currency in self.supported_currencies
