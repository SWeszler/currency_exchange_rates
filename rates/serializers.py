from rest_framework import serializers
from .models import Currency, Rate


class RateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rate model
    """
    currency = serializers.StringRelatedField()
    base_currency = serializers.CharField()
    rate = serializers.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        model = Rate
        exclude = ('id',)

class RateOnlySerializer(RateSerializer):
    """
    Serializer for the Rate model
    """

    class Meta:
        model = Rate
        fields = ('rate', 'date')


class CurrencySerializer(serializers.ModelSerializer):
    """
    Serializer for the Currency model
    """
    rates = RateOnlySerializer(many=True)

    class Meta:
        model = Currency
        fields = ('symbol','rates')
