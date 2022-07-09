from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('cart/', views.cart, name="cart"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('terms/', views.terms, name="terms"),
    path('products/{id}', views.single, name="single"),
    path('update_item/', views.update_item, name="update_item")
]
