from rest_framework import serializers

from src.apps.cars.models import Car, Picture, Color, Model, Brand, FuelType
from src.apps.dealers.serializers import DealerSerializer


class PictureCarSerializer(serializers.Serializer):
    url = serializers.CharField()


class ColorCarSerializer(serializers.Serializer):
    name = serializers.CharField()


class BrandCarSerializer(serializers.Serializer):
    name = serializers.CharField()


class ModelCarSerializer(serializers.Serializer):
    name = serializers.CharField()
    brand = BrandCarSerializer()


class FuelTypeCarSerializer(serializers.Serializer):
    name = serializers.CharField()


class CarListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = ModelCarSerializer()
    dealer = DealerSerializer()


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Model
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class FuelTypeSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = FuelType
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ['url']


class CarCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    picture = PictureSerializer()
    model = ModelSerializer()