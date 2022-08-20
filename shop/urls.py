from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('terms/', views.terms, name="terms"),
    path('products/', views.products, name="products"),
    path('products/<int:id>/', views.single, name="single"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('user_profile/', views.userPage, name="user"),
    path('order_execute/', views.executeOrder, name="order_execute")
]
