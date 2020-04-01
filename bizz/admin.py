from django.contrib import admin
from .models import Category,Location, Image, Post

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Post)

