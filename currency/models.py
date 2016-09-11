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
    currency_rate = models.FloatField(default=0)
    #final currency is nation's currency to krw
    currency_final = models.FloatField(default=0)
    pub_date = models.DateField('published date', default=datetime.date.today())
    
    def __str__(self):  # __str__ on python3
        return self.nation
    
    class Meta:
        abstract = True    
    
#currency of EURO
class CurrencyEUR(CurrencyModel):
    nation = models.CharField(max_length=3, default='EUR')

#currency of Korean Won        
class CurrencyKRW(CurrencyModel):
     nation = models.CharField(max_length=3, default='KRW')
    
#currency of Chinese Yuan    
class CurrencyCNY(CurrencyModel):
     nation = models.CharField(max_length=3, default='CNY')
    
#currency of Japanese Yen
class CurrencyJPY(CurrencyModel):
     nation = models.CharField(max_length=3, default='JPY')
    
#currency of British Pound    
class CurrencyGBP(CurrencyModel):
     nation = models.CharField(max_length=3, default='GBP')
    

    