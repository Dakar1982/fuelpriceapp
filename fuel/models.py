from django.db import models

class Fuel(models.Model):
    city = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.city} - {self.fuel_type}"
