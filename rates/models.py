from django.db import models
from django.conf import settings


class Currency(models.Model):
    """
    Model for currency
    """
    symbol = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.symbol


class Rate(models.Model):
    """
    Model for the rates table.
    """
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='rates',
        null=True,
    )
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateTimeField()
    base_currency = settings.BASE_CURRENCY

    def __str__(self):
        return f'{self.currency} {self.rate}'
