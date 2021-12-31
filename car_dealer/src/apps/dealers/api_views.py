from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.generics import ListAPIView, RetrieveAPIView

from src.apps.cars.models import Car
from src.apps.dealers.helpful_functions import get_list_of_statistic_detail, get_list_of_statistic_list
from src.apps.dealers.paginations import CustomPagination


class StatisticAllView(ListAPIView):
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Car.objects.filter(dealer__user=self.request.user, status_public=True)

    def list(self, request, *args,**kwargs):
        if request.query_params.get('sort'):
            sort = request.query_params.get('sort')
        else:
            sort = 'days'
        list_of_cars_views = [queryset.view_for_statistic for queryset in self.get_queryset()]
        list_of_dict = get_list_of_statistic_list(list_of_cars_views,sort=sort)
        self.paginator.orphans = 4
        data = self.paginate_queryset(list_of_dict)
        return self.get_paginated_response(data)


class StatisticByCarView(RetrieveAPIView):
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'car_pk'

    def get_queryset(self):
        return Car.objects.filter(dealer__user=self.request.user, status_public=True)

    def retrieve(self, request, *args, **kwargs):
        if request.query_params.get('sort'):
            sort = request.query_params.get('sort')
        else:
            sort = 'days'
        views_of_car = self.get_object().view_for_statistic
        list_of_dict = get_list_of_statistic_detail(views_of_car, sort=sort)
        self.paginator.orphans = 4
        data = self.paginate_queryset(list_of_dict)
        return self.get_paginated_response(data)