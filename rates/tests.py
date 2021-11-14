from django.test import TestCase, RequestFactory
from rates.views import RateViewSet


class FetchingRatesTest(TestCase):
    fixtures = ['rates.json']

    def setUp(self):
        self.factory = RequestFactory()

    def test_rates_viewset(self):
        request = self.factory.get('/rates/')
        response = RateViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.data['results'][0]['currency'], 'USD')
        self.assertEqual(response.data['results'][0]['rate'], 1.1448)
