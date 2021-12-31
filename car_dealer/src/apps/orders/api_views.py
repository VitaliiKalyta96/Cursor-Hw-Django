from django.core.mail import send_mail

from rest_framework import generics
from rest_framework.exceptions import ValidationError

from src.apps.orders.serializers import OrderSerializer
from src.apps.orders.models import Order


class OrderApiView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []

    def perform_create(self, serializer):
        data = serializer.validated_data
        try:
            order = Order.objects.get(
                car=data.get('car'),
                phone=data.get('phone'),
                email=data.get('email'),
            )
            if order:
                raise ValidationError('You are have order about this car')
        except Order.DoesNotExist:
            pass
        send_mail('Order for car', 'You order is created successfully', [data.get('email')])
        serializer.save()
