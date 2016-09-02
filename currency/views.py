from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import View
from django.http import HttpResponse
from currency.models import Currency
import requests
import json
import urllib2

class CurrencyIndexView(View):
    def get(self, request):
        opposite_nation = "EUR"
        currency = Currency()
        currency.save()
        currency.opposite_nation = opposite_nation
        json_object = "https://openexchangerates.org/api/historical/2016-08-31.json?app_id=548749f027434cde84582df98bb8df5b"
        recived_object = urllib2.urlopen(json_object)
        recived_data = json.loads(recived_object.read())
        currency.currency_krw = float(recived_data["rates"]["KRW"])
        currency.currency_opposite = float(recived_data["rates"][opposite_nation])
        currency.currency_final = currency.currency_krw/currency.currency_opposite
        currency.save()
        
        return render(request, 'currency/index.html', {'currency': currency})
        