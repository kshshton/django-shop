from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('cart/', views.cart, name="cart"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('terms/', views.terms, name="terms"),
    path('products/<int:id>/', views.single, name="single"),
    path('user_profile/', views.userPage, name="user"),
    path('update_item/', views.update_item, name="update_item")
]
