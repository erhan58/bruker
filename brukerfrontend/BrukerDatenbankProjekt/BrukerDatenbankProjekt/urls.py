"""
Definition of urls for BrukerDatenbankProjekt.
"""

from django.conf.urls import include, url
from Frontend.views import mspListView
from Frontend.views import speciesgenusListView
from Frontend.views import strainListView
from Frontend.views import customerListView
from Frontend.views import dnasequenceListView
from Frontend.views import measurementListView
from Frontend.views import measuringdeviceListView
from Frontend.views import synonymListView
from Frontend.views import logcustomerListView
from django.urls import path



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from Frontend import views

urlpatterns = [
    # Examples:
    # url(r'^$', BrukerDatenbankProjekt.views.home, name='home'),
    # url(r'^BrukerDatenbankProjekt/', include('BrukerDatenbankProjekt.BrukerDatenbankProjekt.urls')),
    
    # Home view
    url(r'^$', views.home, name='home'),
    # url(r'^Speciesgenus/', speciesgenusListView.as_view()),
    path('Speciesgenus/', speciesgenusListView.as_view(), name = 'speciesgenus'),
    path('Msp/', mspListView.as_view(), name = 'msp'),
    path('Strain/', strainListView.as_view(), name = 'strain'),
    path('Customer/', customerListView.as_view(), name = 'customer'),
    path('Dnasequence/', dnasequenceListView.as_view(), name = 'dnasequence'),
    path('Measurement/', measurementListView.as_view(), name = 'measurement'),
    path('Measuringdevice/', measuringdeviceListView.as_view(), name = 'measuringdevice'),
    path('Synonym/', synonymListView.as_view(), name = 'synonym'),
    path('Logcustomer/', logcustomerListView.as_view(), name= 'logcustomer'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls, name= 'admin'),
]
