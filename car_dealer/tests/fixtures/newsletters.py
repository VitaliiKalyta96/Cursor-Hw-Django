import factory

from apps.newsletters.models import NewsLetter


class NewsLetterFactory(factory.DjangoModelFactory):
    email = factory.Sequence(lambda n: 'person{}@example.com'.format(n).lower())

    class Meta:
        model = NewsLetter
