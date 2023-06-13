from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Fuel

class FuelListView(ListView):
    model = Fuel
    template_name = 'fuel/fuel_list.html'
    context_object_name = 'fuel_list'

class FuelDetailView(DetailView):
    model = Fuel
    template_name = 'fuel/fuel_detail.html'
    context_object_name = 'fuel'

class FuelCreateView(CreateView):
    model = Fuel
    template_name = 'fuel/fuel_create.html'
    fields = ['city', 'fuel_type', 'price']
    success_url = reverse_lazy('fuel:fuel_list')

class FuelSortView(ListView):
    model = Fuel
    template_name = 'fuel/fuel_sort.html'
    context_object_name = 'fuel_list'

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by')
        queryset = super().get_queryset()
        
        if sort_by == 'price':
            queryset = queryset.order_by('price')
        elif sort_by == 'name':
            queryset = queryset.order_by('city')
        
        return queryset
