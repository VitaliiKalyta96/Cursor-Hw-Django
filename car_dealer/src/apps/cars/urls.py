from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from src.apps.cars import views, api_views

app_name = 'cars'


api_patterns = [
    path('token-auth/', obtain_auth_token),
    path('cars/', api_views.CRUDCarView.as_view({'post': 'create', 'get': 'list'})),
    path('car/<int:car_pk>', api_views.CRUDCarView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),

    path('colors/', api_views.CRUDColorView.as_view({'post': 'create', 'get': 'list'})),
    path('color/<int:color_pk>', api_views.CRUDColorView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),

    path('brands/',api_views.CRUDBrandView.as_view({'post': 'create', 'get': 'list'})),
    path('brand/<int:brand_pk>',api_views.CRUDBrandView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),

    path('models/', api_views.CRUDModelView.as_view({'post': 'create', 'get': 'list'})),
    path('model/<int:model_pk>',api_views.CRUDModelView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),

    path('fueltypes/',api_views.CRUDColorView.as_view({'post': 'create', 'get': 'list'})),
    path('fueltype/<int:fueltype_pk>',api_views.CRUDColorView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),

    path('cars/', api_views.ApiCarPublicListView.as_view({'get': 'list'})),
    path('car/<int:car_pk>', api_views.ApiCarPublicListView.as_view({'get': 'detail'})),
]

urlpatterns = [
    path('', views.list_cars_view,),
    path('<int:car_pk>/', views.DetailCarView.as_view(), name='detail'),
]