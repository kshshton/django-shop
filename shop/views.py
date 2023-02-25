from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import cart_data
from .forms import CreateUserForm
import datetime
import json


def home(request):
    return render(request, 'shop/home.html')


def products(request):
    data = cart_data(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems,
        }
    return render(request, 'shop/products.html', context)


@login_required(login_url='login')
def cart(request):
    data = cart_data(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'shop/cart.html', context)


@login_required(login_url='login')
def checkout(request):
    data = cart_data(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, context)


def login_page(request):
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
        return render(request, 'shop/login.html')


@login_required(login_url='login')
def logout_user(request):
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
    return render(request, 'shop/register.html', context = {'form': form})


def single(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/single.html', context = {'product': product})


def terms(request):
    return render(request, 'shop/terms.txt')


@login_required(login_url='login')
def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    print('Action: ', action)
    print('productId: ', productId)

    if action == "add":
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()
    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse('Item added', safe=False)


def user_page(request):
    customer = request.user.customer
    order = Order.objects.filter(customer=customer)
    return render(request, 'shop/user.html', context = {
        'customer': customer,
        'order': order,
    })


def order_execute(request):
    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if customer.balance - order.get_cart_total <= 0:
            raise Exception('Niewystarczająca ilość funduszy na koncie...')
        else:
            customer.balance -= order.get_cart_total
        customer.save()
        order.complete = True
        order.transaction_id = transaction_id
        order.save()
    else:
        print('User is not logged in')
    return JsonResponse('Transaction executed!', safe=False)


def add_funds(request):
    deposit = request.POST.get('deposit')
    if request.user.is_authenticated:
        customer = request.user.customer
        if float(deposit) > 0:
            customer.balance += float(deposit)
            print('Funds has been added!')
            customer.save()
    else:
        print('User is not logged in')
    return redirect('user')