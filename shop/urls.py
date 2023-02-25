from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('terms/', views.terms, name="terms"),
    path('products/', views.products, name="products"),
    path('products/<int:id>/', views.single, name="single"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.update_item, name="update_item"),
    path('user_profile/', views.user_page, name="user"),
    path('order_execute/', views.order_execute, name="order_execute"),
    path('add_funds/', views.add_funds, name="add_funds")
]
