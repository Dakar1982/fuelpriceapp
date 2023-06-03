"""
URL configuration for fuelpriceapp project.

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

from django.contrib import admin
from django.urls import path
from .apps.fuel.views import FuelPriceListView, FuelPriceCreateView, add_fuel_price

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fuel/', FuelPriceListView.as_view(), name='fuel_price_list'),
    path('fuel/add/', FuelPriceCreateView.as_view(), name='fuel_price_create'),
    path('fuel/add_fuel/', add_fuel_price, name='add_fuel_price'),
]
