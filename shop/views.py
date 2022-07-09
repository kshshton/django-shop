from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *


def home(request):
    context = {}
    return render(request, 'shop/home.html', context)


def products(request):
    items = Product.objects.all()
    context = { 'items': items }
    return render(request, 'shop/products.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'shop/cart.html', context)


def login(request):
    context = {}
    return render(request, 'shop/login.html', context)


def register(request):
    context = {}
    return render(request, 'shop/register.html', context)


def single(request):
    context = {}
    return render(request, 'shop/single-id.html', context)


def terms(request):
    context = {}
    return render(request, 'shop/terms.txt', context)


def update_item(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']

    print('Action: ', action)
    print('itemId: ', itemId)

    customer = request.user.customer
    product = Product.objects.get(id=itemId)
    order, created = Order.objects.get_or_create(cu)
    return JsonResponse('Item added', safe=False)