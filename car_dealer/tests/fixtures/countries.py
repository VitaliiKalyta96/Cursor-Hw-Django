import factory
from factory import fuzzy

from src.apps.countries.models import Country, City


class CountryFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()

    class Meta:
        model = Country


class CityFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = City