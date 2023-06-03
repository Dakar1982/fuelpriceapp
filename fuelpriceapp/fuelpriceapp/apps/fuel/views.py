from django.views.generic import ListView, CreateView
from .models import FuelPrice
from django.shortcuts import render


class FuelPriceListView(ListView):
    model = FuelPrice
    template_name = 'fuel/price_list.html'
    context_object_name = 'fuel_prices'

class FuelPriceCreateView(CreateView):
    model = FuelPrice
    template_name = 'fuel/price_create.html'
    fields = ['fuel_type', 'price']


def add_fuel_price(request):
    # Kod obsługujący żądanie
    return render(request, 'fuel/add_fuel_price.html')
