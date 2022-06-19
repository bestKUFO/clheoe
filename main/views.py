from django.shortcuts import render
from .models import Order


def base(request):
    order_list = Order.objects.all()
    order = {'order_list': order_list}

    return render(request, "main/base.html", order)


def item(request):
    return render(request, "main/item.html")


def terms(request):
    return render(request, "main/terms.html")


def membership(request):
    return render(request, "main/membership.html")


def privacy(request):
    return render(request, "main/privacy.html")


def executives(request):
    return render(request, "main/executives.html")


def service(request):
    return render(request, "main/service.html")
