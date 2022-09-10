from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import cookieCart, cartData
from .forms import CreateUserForm
import datetime
import json


def home(request):
    context = {}
    return render(request, 'shop/home.html', context)


def products(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'shop/products.html', context)


@login_required(login_url='login')
def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'shop/cart.html', context)


@login_required(login_url='login')
def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'shop/checkout.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Incorrect data')

        context = {}
        return render(request, 'shop/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account {username} has been created')
            user = form.save()
            Customer.objects.create(user=user, name=username, email=email)
            return redirect('login')


    context = {'form': form}
    return render(request, 'shop/register.html', context)


def single(request, id):
    product = Product.objects.get(id=id)

    context = {'product': product}
    return render(request, 'shop/single.html', context)


def terms(request):
    context = {}
    return render(request, 'shop/terms.txt', context)


@login_required(login_url='login')
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('productId: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item added', safe=False)


def userPage(request):
    customer = request.user.customer
    order = Order.objects.filter(customer=customer)

    context = {'customer': customer, 'order': order}

    return render(request, 'shop/user.html', context)


def executeOrder(request):
    transaction_id = datetime.datetime.now().timestamp()

    def executeTrasaction():
        if customer.balance - order.get_cart_total <= 0:
            raise Exception('Niewystarczająca ilość funduszy na koncie...')
        else:
            customer.balance -= order.get_cart_total

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        executeTrasaction()
        customer.save()

        order.complete = True
        order.transaction_id = transaction_id
        order.save()

    else:
        print('User is not logged in')

    return JsonResponse('Transaction executed!', safe=False)


def addFunds(request):
    deposit = request.POST.get('deposit')

    if request.user.is_authenticated:
        customer = request.user.customer
        customer.balance += float(deposit)
        print('Funds has been added!')
        customer.save()
    else:
        print('User is not logged in')

    
    return redirect('user')
