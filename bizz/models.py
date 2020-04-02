from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    contact = models.CharField(max_length =30)
    price = models.FloatField()
    pub_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

CATEGORY_CHOISES = (
    ('B','Bed'),
    ('C','Chair'),
    ('T','Table')
)

LABEL_CHOISES = (
    ('p','Primary'),
    ('S','Secondary'),
    ('D','Danger')
)

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOISES, max_length=2)
    label = models.CharField(choices=LABEL_CHOISES, max_length=2)
    contact = models.CharField(max_length =30)
    quantity = models.IntegerField(default=1)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product')

    def get_add_to_cart_url(self):
        return reverse('add_to_cart')
        
        
class OrderPost(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.post.title}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    posts = models.ManyToManyField(OrderPost)
    pub_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username


