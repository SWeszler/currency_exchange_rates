from .models import Rate, Currency
from .serializers import RateSerializer, CurrencySerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response


class CurrencyViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows currencies to be viewed.
    """
    queryset = Currency.objects.all().prefetch_related('rates')
    serializer_class = CurrencySerializer
    lookup_field = 'symbol'


class RateViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows rates to be viewed.
    """
    queryset = Rate.objects.all().order_by('-date').prefetch_related('currency')
    serializer_class = RateSerializer
    lookup_field = 'currency'

    def retrieve(self, request, *args, **kwargs):
        """
        Return the latest rate for a given currency.
        """
        queryset = self.get_queryset()
        currency = kwargs['currency']
        queryset = queryset.filter(currency__symbol=currency)
        if 'date' in kwargs:
            queryset = queryset.filter(date=kwargs['date'])

        rate = queryset.first()
        if not rate:
            return Response(status=404)

        serializer = self.get_serializer(rate)
        return Response(serializer.data)
