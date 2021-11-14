from .models import Rate
from .serializers import RateSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response


class RateViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows rates to be viewed.
    """
    queryset = Rate.objects.all().order_by('-date')
    serializer_class = RateSerializer
    lookup_field = 'currency'

    def retrieve(self, request, *args, **kwargs):
        """
        Return the latest rate for a given currency.
        TODO - change it to list all rates for a given currency.
        """
        queryset = self.get_queryset()
        currency = kwargs['currency']
        queryset = queryset.filter(currency=currency)
        if 'date' in kwargs:
            queryset = queryset.filter(date=kwargs['date'])

        rate = queryset.first()
        if not rate:
            return Response(status=404)

        serializer = self.get_serializer(rate)
        return Response(serializer.data)
