from django.test import TestCase
from rest_framework.test import APIRequestFactory


class FetchingRatesTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_fetching_rates(self):
        request = self.factory.get('/rates/')
        print(request)
