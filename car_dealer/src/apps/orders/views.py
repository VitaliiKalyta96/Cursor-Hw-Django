from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView
from src.apps.orders.models import Order


# @login_required
def list_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/list.html', {'orders': orders})


class DetailOrderView(DetailView):
    model = Order
    template_name = 'orders/detail.html'
    pk_url_kwarg = 'order_pk'
    context_object_name = 'order'
