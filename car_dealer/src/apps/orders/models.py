from django.db import models
from django.conf import settings

from src.apps.dealers.models import Dealer


class Order(models.Model):
    STATUS_IN_STOCK = 'in_stock'
    STATUS_SOLD = 'sold'

    STATUS_CHOICES = (
        (STATUS_IN_STOCK, "In stock"),
        (STATUS_SOLD, "Sold"),
    )

    order_id = models.IntegerField(primary_key=True, verbose_name="ID")
    car_id = models.ForeignKey('cars.Car', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_IN_STOCK)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone = models.IntegerField()
    message = models.TextField()