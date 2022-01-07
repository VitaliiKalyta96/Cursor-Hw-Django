from django.contrib import admin

from src.apps.countries.models import Country, City


admin.site.register(Country)
admin.site.register(City)
