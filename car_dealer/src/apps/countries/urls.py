from django.urls import path
from src.apps.countries import views


urlpatterns = [
    path('', views.main_page, ),
    ]