from django import forms
from currency.models import Choice
from django.shortcuts import render
from currency.models import CurrencyKRW, CurrencyEUR, Choice, CurrencyModel, CurrencyCNY, CurrencyJPY, CurrencyGBP
from django.utils import timezone
import json
import urllib2
import datetime
import unicodedata

class InputValueForm(forms.Form):
    used_amount_field = forms.CharField(label="Used Amount")
    choice_datas=Choice.objects.all()
    choice_list=[]
    for choice in choice_datas:
        choice_list.append((choice , choice.choice_text))
    #for choice in choice_datas:
     #   choice_list.append(choice.choice_text)
    select_currency_field = forms.ChoiceField(choices=choice_list, widget=forms.Select(), label="Now Currency")
    
    #Control when form is submitted
    def submitted(self, request):
        used_amount = request.POST['used_amount_field']
        #used_amount_string = unicodedata.normalize('NFKD', used_amount).encode('ascii','ignore')
        selected_currency = request.POST.get('select_currency_field')
        #selected_currency_string = unicodedata.normalize('NFKD', selected_currency).encode('ascii','ignore')
        #render(request, 'currency/result.html', {'used_amount':used_amount, 'selected_currency':selected_currency})
        currencyModel_list = [CurrencyKRW.objects.last(), CurrencyEUR.objects.last(), CurrencyCNY.objects.last(), CurrencyJPY.objects.last(), CurrencyGBP.objects.last()]
        selected_currency_model = currencyModel_list[0]
        for currencymodel in currencyModel_list:
            if currencymodel.nation==selected_currency:
                selected_currency_model = currencymodel
        lastcurrency = selected_currency_model
        
        today=datetime.date.today()
        if lastcurrency.pub_date==datetime.date.today():
            lastcurrency.currency_final = CurrencyKRW.objects.last().currency_rate/lastcurrency.currency_rate
            lastcurrency.save()
        else:
            currencyeur = CurrencyEUR()
            currencykrw = CurrencyKRW()
            currencycny = CurrencyCNY()
            currencyjpy = CurrencyJPY()
            currencygbp = CurrencyGBP()
            json_object = "https://openexchangerates.org/api/latest.json?app_id=548749f027434cde84582df98bb8df5b"
            recived_object = urllib2.urlopen(json_object)
            recived_data = json.loads(recived_object.read())
            currencyeur.currency_rate = float(recived_data["rates"]["EUR"])
            currencykrw.currency_rate = float(recived_data["rates"]["KRW"])
            currencycny.currency_rate = float(recived_data["rates"]["CNY"])
            currencyjpy.currency_rate = float(recived_data["rates"]["JPY"])
            currencygbp.currency_rate = float(recived_data["rates"]["GBP"])
            currencyeur.save()
            currencykrw.save()
            currencycny.save()
            currencyjpy.save()
            currencygbp.save()
            lastcurrency.currency_final = CurrencyKRW.objects.last().currency_rate/lastcurrency.currency_rate
            lastcurrency.save()
        return render(request, 'currency/result.html', {'currency': lastcurrency})