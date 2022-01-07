from django.urls import path
from .views import NewsLetterView, success_subscribe

app_name = 'newsletters'

urlpatterns = [
    path('new/', NewsLetterView.as_view(), ),
    path('success/', success_subscribe, ),
    path('<str:email>/', success_subscribe, ),
]