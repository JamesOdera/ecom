from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post, OrderPost, Order 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, 'index.html')

def item_list(request):
    items = Item.objects.all()
    # context = {
    #     'items': Item.objects.all()
    # }
    return render(request, 'item_list.html', { 'items': items})

def checkout(request):
    return render(request, 'checkout-page.html')

@login_required
def product(request):
    items = Item.objects.all()
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'product.html',{ 'items': items}, context)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-pub_date']
    template_name = 'product.html'

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [ 'title', 'description', 'price', 'contact', 'category','label', 'cover']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [ 'title', 'description', 'price', 'contact', 'category', 'location', 'cover']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/product' 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def add_to_cart(request, int:'pk'):
    post = get_object_or_404(Post, pk=pk)
    order_post = OrderPost.objects.create(post=post)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.posts.filter(post__pk=post.pk).exists():
            order_post.quantity += 1
            order_post.save()
    else:
        order = order.objects.create(user=request.user)
        order.posts.add(order_post)

    return redirect('post-detail', int)
