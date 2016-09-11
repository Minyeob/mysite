from django import forms
from currency.models import Choice

class InputValueForm(forms.Form):
    inputvaluefield = forms.CharField(label="used value")
    selectcurrencyfield = forms.ChoiceField(widget=forms.RadioSelect, choices=Choice.objects.all())
    
    #Control when form is submitted
    def submitted(self, request):
        a=Choice.objects.last()