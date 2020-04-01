from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post 

def index(request):
    return render(request, 'index.html')

@login_required
def product(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'product.html', context)
