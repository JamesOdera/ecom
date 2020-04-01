from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns=[
    path('',views.index,name = 'index'),
    path('product',PostListView.as_view(),name = 'product'),
    path('post/<int:pk>',PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)