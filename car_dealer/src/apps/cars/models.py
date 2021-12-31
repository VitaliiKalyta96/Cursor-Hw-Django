from django.db import models
from django.conf import settings

from src.apps.dealers.models import Dealer


class Car(models.Model):
    STATUS_IN_STOCK = 'in_stock'
    STATUS_SOLD = 'sold'

    STATUS_CHOICES = (
        (STATUS_IN_STOCK, "In stock"),
        (STATUS_SOLD, "Sold"),
    )

    CHOICE_AA = 'A+'
    CHOICE_A = 'A'
    CHOICE_B = 'B'
    CHOICE_C = 'C'
    CHOICE_D = 'D'
    CHOICE_E = 'E'
    CHOICE_F = 'F'
    CHOICE_G = 'G'

    CHOICES = (
        (CHOICE_AA, "A+"),
        (CHOICE_A, "A"),
        (CHOICE_B, "B"),
        (CHOICE_C, "C"),
        (CHOICE_D, "D"),
        (CHOICE_E, "E"),
        (CHOICE_F, "F"),
        (CHOICE_G, "G"),
    )

    car_id = models.IntegerField(primary_key=True)
    color_id = models.ForeignKey('cars.Color', on_delete=models.CASCADE)
    dealer_id = models.ForeignKey('dealers.Dealer', on_delete=models.SET_NULL, null=True)
    model_id = models.ForeignKey('cars.Model', on_delete=models.CASCADE, null=True)
    fuel_type_id = models.ForeignKey('cars.FuelType', on_delete=models.CASCADE, null=True)
    engine_type = models.CharField(max_length=30)
    pollutant_class = models.CharField(max_length=20, choices=CHOICES, default=CHOICE_AA)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_IN_STOCK)
    door = models.CharField(max_length=20)
    capacity = models.CharField(max_length=25)
    gear_case = models.CharField(max_length=20)
    number = models.IntegerField()
    slug = models.CharField(max_length=20)
    sitting_place = models.IntegerField()
    first_registration_date = models.DateTimeField(auto_now=False)
    engine_power = models.CharField(max_length=20)
    other = models.TextField()

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Picture(models.Model):
    picture_id = models.IntegerField(primary_key=True)
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=15)
    metadata = models.CharField(max_length=15)
    url = models.URLField(max_length=200)


class Color(models.Model):
    color_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Model(models.Model):
    model_id = models.IntegerField(primary_key=True)
    brand_id = models.ForeignKey('cars.Brand', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    property_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class CarProperty(models.Model):
    car_property_id = models.IntegerField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)


class FuelType(models.Model):
    CHOICE_1 = 'gas'
    CHOICE_2 = 'diesel'
    CHOICE_3 = 'gasoline'
    CHOICE_4 = 'electro'

    CHOICE_FUEL_TYPE = (
        (CHOICE_1, "Gas"),
        (CHOICE_2, "Diesel"),
        (CHOICE_3, "Gasoline"),
        (CHOICE_4, "Electro"),
    )
    fuel_type_id = models.IntegerField(primary_key=True, verbose_name='ID')
    type = models.CharField(max_length=40, choices=CHOICE_FUEL_TYPE, default=CHOICE_2, verbose_name='Fuel type')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Fuel type'
        verbose_name_plural = 'Fuel types'
