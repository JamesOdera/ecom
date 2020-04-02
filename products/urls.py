from django.urls import path, include
from . views import Home
from cart.views import add_to_cart, remove_from_cart
app_name= 'mainapp'

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]