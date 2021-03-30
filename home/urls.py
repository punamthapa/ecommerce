from django.urls import path
from .views import *

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('product-list', productlist, name='product-list'),
    path('product-detail', productdetail, name='product-detail'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('my-account', myaccount, name='my-account'),
    path('login', login, name='login'),
    path('wishlist', wishlist, name='wishlist'),
    path('contact', contact, name='contact'),



]