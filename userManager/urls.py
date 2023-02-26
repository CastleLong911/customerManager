

from django.urls import path
from . import views

app_name='login'

urlpatterns=[
    path('', views.loginPage, name='loginPage'),
    path('login/', views.loginUser, name='login_user'),
    path('logout/', views.logoutUser, name='logout_user'),
]