from __future__ import unicode_literals
from django.db import models

class Currency(models.Model):
    opposite_nation = models.CharField

    #Base money is korean 'won'
    currency_krw = models.FloatField

    #currency of opposite nation to 'USD'
    currency_opposite = models.FloatField

    #currency of 'KRW' to 'Opposite nation's money'
    currency_final = models.FloatField

    def __str__(self):  # __str__ on python3
        return self.question_text