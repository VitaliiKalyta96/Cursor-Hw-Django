import factory
from factory import fuzzy

from apps.orders.models import Order
from apps.cars.models import Car


class OrderFactory(factory.DjangoModelFactory):
    first_name = 'Jack'
    last_name = 'Redis'
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.first_name, a.last_name).lower())
    phone = factory.Sequence(lambda n: '380-%09d' % n)
    message = fuzzy.FuzzyText()

    class Meta:
        model = Order


class CarFactory(factory.DjangoModelFactory):
    car = factory.SubFactory(OrderFactory)

    class Meta:
        model = Car
