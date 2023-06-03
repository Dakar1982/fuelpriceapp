"""
URL configuration for FuelPrice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'fuel'

urlpatterns = [
    path('', views.FuelPriceListView.as_view(), name='price_list'),
    path('add/', views.FuelPriceCreateView.as_view(), name='price_create'),
    path('fuel/add/', add_fuel_price, name='add_fuel_price'),

]
