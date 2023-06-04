from django.views.generic import ListView, CreateView
from .models import FuelPrice
from django.shortcuts import render
from django.urls import reverse_lazy



class FuelPriceListView(ListView):
    model = FuelPrice
    template_name = 'fuel/price_list.html'
    context_object_name = 'fuel_prices'

class FuelPriceCreateView(CreateView):
    model = FuelPrice
    template_name = 'fuel/price_create.html'
    fields = ['fuel_type', 'price']
    success_url = reverse_lazy('add_fuel_price')



def add_fuel_price(request):
    # Kod obsługujący żądanie
    return render(request, 'fuel/add_fuel_price.html')
