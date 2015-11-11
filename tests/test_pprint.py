from unittest import TestCase

from pandas_frequency_prettyprinter import pprint


class PprintTestCase(TestCase):

    def test_day(self):
        self.assertEqual(pprint('D', '1 day'))
        self.assertEqual(pprint('1D', '1 day'))
        self.assertEqual(pprint('18D', '18 days'))

    def test_business_day(self):
        self.assertEqual(pprint('B', '1 business day'))
        self.assertEqual(pprint('1B', '1 business day'))
        self.assertEqual(pprint('36B', '36 business days'))

    def test_hour(self):
        self.assertEqual(pprint('H', '1 hour'))
        self.assertEqual(pprint('1H', '1 hour'))
        self.assertEqual(pprint('123H', '123 hours'))

    def test_minute(self):
        self.assertEqual(pprint('T', '1 minute'))
        self.assertEqual(pprint('1T', '1 minute'))
        self.assertEqual(pprint('121T', '121 minutes'))

    def test_second(self):
        self.assertEqual(pprint('S', '1 second'))
        self.assertEqual(pprint('1S', '1 second'))
        self.assertEqual(pprint('100S', '100 seconds'))

    def test_millisecond(self):
        self.assertEqual(pprint('L', '1 millisecond'))
        self.assertEqual(pprint('1L', '1 millisecond'))
        self.assertEqual(pprint('100L', '100 milliseconds'))

    def test_microsecond(self):
        self.assertEqual(pprint('U', '1 microsecond'))
        self.assertEqual(pprint('1U', '1 microsecond'))
        self.assertEqual(pprint('100U', '100 microseconds'))

    def test_month(self):
        # Anchored at last day of month
        self.assertEqual(pprint('M', '1 month, anchored at last day of month'))
        self.assertEqual(pprint('1M',
                                '1 month, anchored at last day of month'))
        self.assertEqual(pprint('10M',
                                '100 months, anchored at last day of month'))

        # Anchored at last business day of month
        self.assertEqual(pprint(
            'BM', '1 month, anchored at last business day of month'))
        self.assertEqual(pprint(
            '1BM', '1 month, anchored at last business day of month'))
        self.assertEqual(pprint(
            '10BM', '100 months, anchored at last business day of month'))

        # Anchored at first day of month
        self.assertEqual(pprint(
            'MS', '1 month, anchored at first day of month'))
        self.assertEqual(pprint(
            '1MS', '1 month, anchored at first day of month'))
        self.assertEqual(pprint(
            '10MS', '100 months, anchored at first day of month'))

        # Anchored at first business day of month
        self.assertEqual(pprint(
            'BMS', '1 month, anchored at first business day of month'))
        self.assertEqual(pprint(
            '1BMS', '1 month, anchored at first business day of month'))
        self.assertEqual(pprint(
            '10BMS', '100 months, anchored at first business day of month'))

        # Anchored at second Tuesday of month
        self.assertEqual(pprint(
            'W-2TUE', '1 month, anchored on second Tuesday'))
        self.assertEqual(pprint(
            '2W-2TUE', '2 months, anchored on second Tuesday'))
        self.assertEqual(pprint(
            '10W-2TUE', '10 months, anchored on second Tuesday'))

    def test_week(self):
        self.assertEqual(pprint('W-TUE', '1 week, anchored on Tuesday'))
        self.assertEqual(pprint('1W-TUE', '1 week, anchored on Tuesday'))
        self.assertEqual(pprint('10W-TUE', '10 weeks, anchored on Tuesday'))

    def test_annual(self):
        # Anchored at end of month
        self.assertEqual(pprint(
            'A-FEB', '1 year, anchored at end of February'))
        self.assertEqual(pprint(
            '1A-FEB', '1 year, anchored at end of February'))
        self.assertEqual(pprint(
            '3A-FEB', '3 years, anchored at end of February'))

        # Anchored at last business day of month
        self.assertEqual(pprint(
            'BA-FEB', '1 year, anchored at last business day of February'))
        self.assertEqual(pprint(
            '1BA-FEB', '1 year, anchored at last business day of February'))
        self.assertEqual(pprint(
            '3BA-FEB', '3 years, anchored at last business day of February'))

        # Anchored at start of month
        self.assertEqual(pprint(
            'AS-FEB', '1 year, anchored at start of February'))
        self.assertEqual(pprint(
            '1AS-FEB', '1 year, anchored at start of February'))
        self.assertEqual(pprint(
            '3AS-FEB', '3 years, anchored at start of February'))

        # Anchored at first business day of month
        self.assertEqual(pprint(
            'BAS-FEB', '1 year, anchored at first business day of February'))
        self.assertEqual(pprint(
            '1BAS-FEB', '1 year, anchored at first business day of February'))
        self.assertEqual(pprint(
            '3BAS-FEB', '3 years, anchored at first business day of February'))
