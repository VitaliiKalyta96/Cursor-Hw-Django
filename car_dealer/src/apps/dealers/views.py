from django.contrib.auth import login, logout
from src.apps.dealers.forms import LoginForm

from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views import View
from src.apps.dealers.models import Dealer


class LoginView(View):
    form = LoginForm

    def get(self, request):
        if not request.user.is_anonymous:
            return HttpResponseRedirect('/')
        return self._login_page(request, context={})

    def _login_page(self, request, context=None):
        context = context or {}
        context['login'] = self.form()

        return render(request=request, template_name='login.html', context=context)

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            login(request, form.cleaned_data['user'])
            return HttpResponseRedirect('/')

        return self._login_page(request, {"errors": form.errors})


class LogoutView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/')
        return self._logout(request)

    def _logout(self, request):
        request.user.auth_token.is_active=False
        logout(request)

        return HttpResponseRedirect('/')


def list_dealers_view(request):
    dealers = Dealer.objects.all().prefetch_related('user')
    return render(request, 'dealers/list.html', {'dealers': dealers})


def detail_dealer_view(request, dealer_pk):
    dealer = Dealer.objects.filter(id=dealer_pk).prefetch_related('dealers_cars__model').first()
    return render(request, 'dealers/detail.html', {'dealer': dealer, })




# from django.shortcuts import render, redirect
# from django.views.generic.edit import FormView
#
# from django.contrib.users.views import LoginView
# from django.contrib.users.forms import AuthenticationForm
#
#
# class AuthenticationModelForm(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'registration/login.html'
#     success_url = 'api-token-users/'



# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
#
#
# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'username': user.username,
#             'password': user.password,
#             'token': token.key,
#         })



# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
#