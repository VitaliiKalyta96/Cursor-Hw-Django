from rest_framework import serializers

from src.apps.dealers.models import Dealer


class DealerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    title = serializers.CharField()

    class Meta:
        model = Dealer