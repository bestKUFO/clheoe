from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Order


def base(request):
    order_list = Order.objects.all()
    order = {'order_list': order_list}

    return render(request, "main/base.html", order)


def detailitem(request):
    return render(request, "main/detailitem.html")
