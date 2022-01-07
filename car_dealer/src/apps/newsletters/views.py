from django.views.generic.edit import FormView
from src.apps.newsletters.models import NewsLetter
from src.apps.newsletters.forms import NewsLetterForm

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


class NewsLetterView(FormView):
    form_class = NewsLetterForm
    template_name = 'subscribe.html'
    success_url = '/subscribe/success/'

    """Note. If you want sign up your email success that subscriber, first of all you must 
    add email in admin directly in apps newsletters."""

    def form_valid(self, form):
        subscriber = form.cleaned_data['email']
        try:
            return redirect('/subscribe/'+NewsLetter.objects.get(email=subscriber).email)
        except(NewsLetter.DoesNotExist,):
            NewsLetter.objects.create(email=subscriber)
        return super().form_valid(form)


def success_subscribe(request, email):
    return render(request, 'success.html', {'email': email})
