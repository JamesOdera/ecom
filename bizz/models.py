from django.db import models
import datetime as dt
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    price =  models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
