import factory
from factory import fuzzy

from src.apps.dealers.models import Dealer
# from apps.countries.models import Country, City
from tests.fixtures.countries import CountryFactory, CityFactory


class DealerFactory(factory.DjangoModelFactory):
    title = fuzzy.FuzzyText()
    email = factory.Sequence(lambda n: 'person{}@example.com'.format(n).lower())
    city = factory.SubFactory(CityFactory)

    class Meta:
        model = Dealer
