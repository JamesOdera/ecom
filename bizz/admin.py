from django.contrib import admin
from .models import Image, Post, OrderPost, Order

admin.site.register(Image)
admin.site.register(Post)
admin.site.register(OrderPost)
admin.site.register(Order)

