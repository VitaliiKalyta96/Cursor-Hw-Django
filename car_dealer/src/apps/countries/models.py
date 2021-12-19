from django.db import models
from django.conf import settings

from src.apps.dealers.models import Dealer


class Country(models.Model):
    contry_id = models.IntegerField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=30)
    code = models.IntegerField()


class City(models.Model):
    city_id = models.IntegerField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=30)
    contry_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name="ID")
