from __future__ import unicode_literals
from django.db import models
import datetime

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    

    def __str__(self): # __str__ on python3
        return self.choice_text
        
#base money is US Dollar
#abstract currency model CurrencyModel
class CurrencyModel(models.Model):
    nation = models.CharField(max_length=3)
    currency_rate = models.FloatField(default=0)
    #final currency is nation's currency to krw
    currency_final = models.FloatField(default=0)
    pub_date = models.DateTimeField('published date')
    pub_date = datetime.date.today()
    
    def __str__(self):  # __str__ on python3
        return self.nation
    
    class Meta:
        abstract = True    
    
#currency of EURO
class CurrencyEUR(CurrencyModel):
    def __init__(self, *args, **kwargs):
        super(CurrencyEUR, self).__init__(*args, **kwargs)
        nation = models.CharField(max_length=3, default='EUR')
        nation.contribute_to_class(self, 'nation')

#currency of Korean Won        
class CurrencyKRW(CurrencyModel):
     def __init__(self, *args, **kwargs):
        super(CurrencyKRW, self).__init__(*args, **kwargs)
        nation = models.CharField(max_length=3, default='KRW')
        nation.contribute_to_class(self, 'nation')
    
#currency of Chinese Yuan    
class CurrencyCNY(CurrencyModel):
     def __init__(self, *args, **kwargs):
        super(CurrencyCNY, self).__init__(*args, **kwargs)
        nation = models.CharField(max_length=3, default='CNY')
        nation.contribute_to_class(self, 'nation')
    
#currency of Japanese Yen
class CurrencyJPY(CurrencyModel):
     def __init__(self, *args, **kwargs):
        super(CurrencyJPY, self).__init__(*args, **kwargs)
        nation = models.CharField(max_length=3, default='JPY')
        nation.contribute_to_class(self, 'nation')
    
#currency of British Pound    
class CurrencyGBP(CurrencyModel):
     def __init__(self, *args, **kwargs):
        super(CurrencyGBP, self).__init__(*args, **kwargs)
        nation = models.CharField(max_length=3, default='GBP')
        nation.contribute_to_class(self, 'nation')
    

    