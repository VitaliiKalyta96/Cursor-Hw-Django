"""car_dealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

# from rest_framework.authtoken import views
# from src.apps.users.views import create_auth_token
# from src.apps.users.views import CustomAuthToken

from src.apps.cars.urls import api_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('apps.countries.urls')),
    path('subscribe/', include('apps.newsletters.urls')),
    # path('api-token-users/', obtain_auth_token),
    # path('api-token-users/', create_auth_token),
    # path('api-token-users/', CustomAuthToken.as_view()),
    path('dealers/', include('apps.dealers.urls')),
    path('cars/', include('apps.cars.urls')),
    path('orders/', include('apps.orders.urls')),
    path('api/', include(api_patterns)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
