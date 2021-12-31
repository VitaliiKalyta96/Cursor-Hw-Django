from django.contrib import admin

from src.apps.cars.models import Car, Picture, Color, Brand, Model, Property, CarProperty, FuelType


admin.site.register(Car)
admin.site.register(Picture)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Property)
admin.site.register(CarProperty)
admin.site.register(FuelType)