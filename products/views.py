from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/home.html'
