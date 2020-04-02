from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, add_to_cart

urlpatterns=[
    path('',views.index,name = 'index'),
    path('product',PostListView.as_view(),name = 'product'),
    path('post/<int:pk>',PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
    path('item_list',views.item_list,name = 'item-list'),
    path('checkout',views.checkout,name = 'checkout'),
    path('add_to_cart',views.add_to_cart,name = 'add_to_cart'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)