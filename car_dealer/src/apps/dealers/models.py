from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# from rest_framework.authtoken.models import Token


class Dealer(AbstractUser):
    dealer_id = models.IntegerField(primary_key=True, verbose_name="ID")
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    city_id = models.ForeignKey('countries.City', on_delete=models.SET_NULL, null=True, verbose_name="ID")

    # class Meta:
    #     proxy = 'rest_framework.authtoken' in settings.INSTALLED_APPS
    #     abstract = 'rest_framework.authtoken' in settings.INSTALLED_APPS
    #     verbose_name = "token"
