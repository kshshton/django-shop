from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .utils import cookieCart, cartData, guestOrder
import json


def home(request):
    context = {}
    return render(request, 'shop/home.html', context)


def products(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    productObjects = Product.objects.all()
    context = {'productObjects': productObjects, 'cartItems': cartItems}
    return render(request, 'shop/products.html', context)

def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
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
    productObjectId = data['productObjectId']
    action = data['action']

    print('Action: ', action)
    print('ProductObjectId: ', productObjectId)

    customer = request.user.customer
    productObject = Product.objects.get(id=productObjectId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, productObject=productObject)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item added', safe=False)