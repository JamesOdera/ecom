from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required 

def index(request):
    return render(request, 'index.html')

@login_required
def product(request):
    return render(request, 'product.html')
