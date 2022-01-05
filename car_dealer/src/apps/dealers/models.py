from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Dealer(AbstractUser):
    dealer_id = models.IntegerField(primary_key=True, verbose_name="ID")
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    city_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="ID")
