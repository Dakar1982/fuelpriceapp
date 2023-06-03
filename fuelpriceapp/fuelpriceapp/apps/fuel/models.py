from django.db import models

class FuelPrice(models.Model):
    fuel_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fuel_type
