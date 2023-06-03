from django.test import TestCase

class FuelPriceTestCase(TestCase):
    def test_fuel_price_creation(self):
        fuel_price = FuelPrice.objects.create(fuel_type='Gasoline', price='2.50')
        self.assertEqual(fuel_price.fuel_type, 'Gasoline')
        self.assertEqual(fuel_price.price, '2.50')
