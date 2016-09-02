from django.conf.urls import patterns, url
from currency import views

urlpatterns = patterns('', 
    url(r'^$', views.CurrencyIndexView.as_view(), name='index'),
    )