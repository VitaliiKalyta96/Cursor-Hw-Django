from django.forms import ModelForm
from src.apps.newsletters.models import NewsLetter


class NewsLetterForm(ModelForm):

    class Meta:

        model = NewsLetter
        fields = ['email']


""" Creating a form to add an article."""
# form = NewsLetter()
#
""" Creating a form to change an existing article."""
# article = NewsLetter.objects.get(pk=1)
# forms = NewsLetterForm(instance=article)
