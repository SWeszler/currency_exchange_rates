from django.db import models


class Rate(models.Model):
    """
    Model for the rates table.
    """
    currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.currency} {self.rate}'
