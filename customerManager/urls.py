

from django.urls import path
from . import views

app_name='customerManager'

urlpatterns=[
    path('', views.loadFind, name='find'),
    path('input/', views.loadInput, name='input'),
    path('inputCustomer/', views.inputCustomer, name='inputCustomer'),
    path('ajaxSearchCustomer/', views.ajax_search_customer, name='ajaxSearchCustomer'),
]