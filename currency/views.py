from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import View
from django.http import HttpResponse
from currency.models import CurrencyKRW, CurrencyEUR, Choice, CurrencyModel, CurrencyCNY, CurrencyJPY, CurrencyGBP
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import requests
import json
import urllib2
import datetime

class CurrencyIndexView(View):
    def get(self, request):
        choice_list = Choice.objects.all()
        return render(request, 'currency/index.html', {'choice_list': choice_list})     

class SelectView(View):
    def post(self, request):
        #lastcurrency = CurrencyKRW.objects.last()
        #if lastcurrency==datetime.date.today():
        choice_id = request.POST['choice']
        selected_choice = Choice.objects.filter(pk=choice_id)
        CurrencyModel_list = [CurrencyKRW, CurrencyEUR, CurrencyCNY, CurrencyJPY, CurrencyGBP]
        for currencymodel in CurrencyModel_list:
            
        lastcurrency = CurrencyModel.objects.filter(nation=selected_choice.choice_text).last()
        if lastcurrency.pub_date==datetime.date.today():
            lastcurrency.currency_final = lastcurrency.currency_rate/CurrencyKRW.objects.last().currency_rate
        else:
            currencyeur = CurrencyEUR()
            currencyeur.save()
            currencykrw = CurrencyKRW()
            currencykrw.save()
            currencycny = CurrencyCNY()
            currencycny.save()
            currencyjpy = CurrencyJPY()
            currencyjpy.save()
            currencygbp = CurrencyGBP()
            currencygbp.save()
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
            lastcurrency.currency_final = lastcurrency.currency_rate/CurrencyKRW.objects.last().currency_rate
        return render(request, 'currency/result.html', {'currency': lastcurrency})    
            
    """def get(self, request):
        currency = CurrencyEUR()
        currency.save()
        json_object = "https://openexchangerates.org/api/latest.json?app_id=548749f027434cde84582df98bb8df5b"
        recived_object = urllib2.urlopen(json_object)
        recived_data = json.loads(recived_object.read())
        currency.currency_krw = float(recived_data["rates"]["KRW"])
        currency.currency_opposite = float(recived_data["rates"][currency.opposite_nation])
        currency.currency_final = currency.currency_krw/currency.currency_opposite
        #currency.pub_date = timezone.now()
        currency.save()
        
        return render(request, 'currency/index.html', {'currency': currency})"""
        
        