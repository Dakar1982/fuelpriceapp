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

from django.urls import path
from fuel.views import FuelListView, FuelDetailView, FuelCreateView, FuelSortView

urlpatterns = [
    
    path('', FuelListView.as_view(), name='fuel_list'),
    path('detail/<int:pk>/', FuelDetailView.as_view(), name='fuel_detail'),
    path('create/', FuelCreateView.as_view(), name='fuel_create'),
    path('sort/', FuelSortView.as_view(), name='fuel_sort'),    
    # path('admin/', admin.site.urls),
    # path('fuel/add/', FuelPriceCreateView.as_view(), name='add_fuel_price'),
    # path('fuel/detail/', FuelPriceListView.as_view(), name='price_list'),  
    # path('fuel/<int:pk>/', FuelDetailView.as_view(), name='fuel-detail'), 
#    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
#    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
#    path('signup/', SignUpView.as_view(), name="signup",),
#    path("fuel/", include("fuel.urls")),
]
