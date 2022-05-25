from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'shop/index.html', context)


def products(request):
    context = {}
    return render(request, 'shop/products.html', context)


def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)


def login(request):
    context = {}
    return render(request, 'shop/login.html', context)


def register(request):
    context = {}
    return render(request, 'shop/register.html', context)
