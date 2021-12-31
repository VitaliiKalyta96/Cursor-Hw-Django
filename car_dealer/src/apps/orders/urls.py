from django.urls import path
from src.apps.orders import views, api_views

urlpatterns = [
    path('', views.list_orders, name='status'),
    path('api/create/', api_views.OrderApiView.as_view(), ),
    path('<order_pk>/', views.DetailOrderView.as_view(),),
]