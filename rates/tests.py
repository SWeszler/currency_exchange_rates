from django.test import TestCase, RequestFactory
from rates.views import RateViewSet


class FetchingRatesTest(TestCase):
    fixtures = ['rates.json']

    def setUp(self):
        self.factory = RequestFactory()

    def test_all_rates(self):
        request = self.factory.get('/rates/')
        response = RateViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.data['results'][0]['currency'], 'USD')
        self.assertEqual(response.data['results'][0]['rate'], '1.1444')

    def test_usd_latest_rate(self):
        request = self.factory.get('/rates/USD/')
        response = RateViewSet.as_view({'get': 'retrieve'})(request, currency='USD')
        self.assertEqual(response.data['currency'], 'USD')
        self.assertEqual(response.data['rate'], '1.1444')
