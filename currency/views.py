from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse
from currency.models import CurrencyKRW, CurrencyEUR, Choice, CurrencyModel, CurrencyCNY, CurrencyJPY, CurrencyGBP
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import requests
import json
import urllib2
import datetime
from currency.forms import InputValueForm

class CurrencyIndexView(FormView):
    template_name = 'currency/currencyindex.html'
    success_url = 'currency:select'
    form_class = InputValueForm
    
    
    #When submit request is handled in html
    """def get(self, request):
        choice_list = Choice.objects.all()
        return render(request, 'currency/index.html', {'choice_list': choice_list})     
    """
class SelectView(View):
    def post(self, request):
        #request.POST is object include data in submitted form
        choice_id = request.POST['choice']
        selected_choice = Choice.objects.get(pk=choice_id)
        currencyModel_list = [CurrencyKRW.objects.last(), CurrencyEUR.objects.last(), CurrencyCNY.objects.last(), CurrencyJPY.objects.last(), CurrencyGBP.objects.last()]
        selected_currency_model = currencyModel_list[0]
        for currencymodel in currencyModel_list:
            if currencymodel.nation==selected_choice.choice_text:
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
            
        
        