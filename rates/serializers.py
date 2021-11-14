from rest_framework import serializers
from .models import Rate


class RateSerializer(serializers.Serializer):
    """
    Serializer for the Rate model
    """
    id = serializers.IntegerField(read_only=True)
    rate = serializers.IntegerField()
    date = serializers.DateTimeField()
    currency = serializers.CharField()
