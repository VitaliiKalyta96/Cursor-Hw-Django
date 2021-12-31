from django.urls import path
from src.apps.dealers import views, api_views

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginView.as_view(),name='login-page'),
    path('logout/', views.LogoutView.as_view()),

    path('', views.list_dealers_view, ),
    path('<dealer_pk>/', views.detail_dealer_view, ),

    path('statistics/', api_views.StatisticAllView.as_view(),),
    path('statistic/<int:car_pk>', api_views.StatisticByCarView.as_view(),),
]
