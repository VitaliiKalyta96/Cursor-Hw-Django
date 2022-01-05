import datetime
from uuid import uuid4

import factory
from factory import fuzzy

from apps.cars.models import Car, Picture, Color, Brand, Model, Property, CarProperty
from apps.orders.models import Order
from tests.fixtures.dealers import DealerFactory


class BrandFactory(factory.DjangoModelFactory):
    # logo = factory.django.ImageField(color='blue')
    name = factory.Sequence(lambda n: 'user%d' % n)

    class Meta:
        model = Brand


class ModelFactory(factory.DjangoModelFactory):
    brand = factory.SubFactory(BrandFactory)
    name = factory.LazyFunction(lambda: uuid4().hex)

    class Meta:
        model = Model


class PictureFactory(factory.DjangoModelFactory):
    picture = factory.SubFactory(BrandFactory)
    position = fuzzy.FuzzyText()
    metadata = fuzzy.FuzzyText()
    url = fuzzy.FuzzyText()


class ColorFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()

    class Meta:
        model = Color


class CarFactory(factory.DjangoModelFactory):
    color = factory.SubFactory(ColorFactory)
    dealer = factory.SubFactory(DealerFactory)
    model = factory.SubFactory(ModelFactory)
    picture = factory.SubFactory(PictureFactory)
    engine_type = fuzzy.FuzzyText()
    price = fuzzy.FuzzyText()
    fuel_type = fuzzy.FuzzyText()
    door = fuzzy.FuzzyText()
    capacity = fuzzy.FuzzyText()
    gear_case = fuzzy.FuzzyInteger(0, 1000, step=1)
    slug = fuzzy.FuzzyText()
    sitting_place = fuzzy.FuzzyInteger(0, 8, step=1)
    first_registration_date = factory.fuzzy.FuzzyDateTime(2021, 12, 18, 20, tzinfo=datetime.datetime)
    engine_power = fuzzy.FuzzyText()
    other = fuzzy.FuzzyText()

    class Meta:
        model = Car


class OrderFactory(factory.DjangoModelFactory):
    car = factory.SubFactory(CarFactory)

    class Meta:
        model = Order


class PropertyFactory(factory.DjangoModelFactory):
    category = fuzzy.FuzzyText()
    name = fuzzy.FuzzyText()

    class Meta:
        model = Property


class CarPropertyFactory(factory.DjangoModelFactory):
    property = factory.SubFactory(PropertyFactory)
    car = factory.SubFactory(CarFactory)

    class Meta:
        model = CarProperty
