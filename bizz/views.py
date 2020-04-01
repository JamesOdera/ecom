from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView 
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin 


def index(request):
    return render(request, 'index.html')

@login_required
def product(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'product.html', context)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-pub_date']
    template_name = 'product.html'

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [ 'title', 'description', 'price', 'contact', 'category', 'location', 'cover']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
