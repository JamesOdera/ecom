from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Order
from django.contrib import messages

class Home(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/home.html'

class OrderSummaryView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object':order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "you dont have an active order")
            return redirect('home')
        

