from django.contrib import admin
from .models import Dealer
from src.apps.countries.models import Country, City
from src.apps.newsletters.models import NewsLetter
from src.apps.cars.models import Car, Picture, Color, Brand, Model, Property, CarProperty
from src.apps.orders.models import Order

# Register your models here.
admin.site.register(Dealer)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(NewsLetter)
admin.site.register(Car)
admin.site.register(Picture)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Property)
admin.site.register(CarProperty)
admin.site.register(Order)