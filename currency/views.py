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
import json
import urllib2
import datetime
from currency.forms import InputValueForm
from django.core.urlresolvers import reverse_lazy
from currency.function import Currency_Setting

#When form is handled by django
class CurrencyIndexView(FormView):
    template_name = 'currency/currencyindex.html'
    success_url = reverse_lazy('currency:select')
    form_class = InputValueForm
    
    def form_valid(self, form):
        form.submitted(self.request)
        return super(CurrencyIndexView, self).form_valid(form)
    
    #When submit request is handled in html
    """def get(self, request):
        choice_list = Choice.objects.all()
        return render(request, 'currency/index.html', {'choice_list': choice_list})     
    """
class SelectView(View):
    def post(self, request):
        form = InputValueForm(request.POST)
        
        if form.is_valid():
            used_amount = form.cleaned_data['used_amount_field']
            selected_currency = form.cleaned_data['select_currency_field']
            #lastcurrency is latest object of selected currency model
            lastcurrency = Currency_Setting().check_selected_currency(selected_currency)
            #check created date of latest object
            datecheck = Currency_Setting().check_created_date(lastcurrency)
            
            #if created date of latest object is today, then use latest object
            if datecheck==True:
                lastcurrency.currency_final = CurrencyKRW.objects.last().currency_rate/lastcurrency.currency_rate
                lastcurrency.save()
            #if created date of latest object is not today, then load new currency data and reload latest object of selected currency model
            else:
                Currency_Setting().load_new_currency()
                lastcurrency = Currency_Setting().check_selected_currency(selected_currency)
                lastcurrency.currency_final = CurrencyKRW.objects.last().currency_rate/lastcurrency.currency_rate
                lastcurrency.save()
        
        used_amount_to_krw = lastcurrency.currency_final * used_amount
        return render(request, 'currency/result.html', {'currency': lastcurrency, 'used_amount_to_krw': used_amount_to_krw, 'used_amount': used_amount})
        
        
        #When form is handled by html
        """
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
        """
        
        