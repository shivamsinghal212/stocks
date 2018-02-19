from django.db import models
# Create your models here.


class HistStocks(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.symbol
