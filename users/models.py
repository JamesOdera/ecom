from django.db import models

class User(models.Model):
    username = models.CharField(max_length =60)
    firstname = models.CharField(max_length =60)
    lastname = models.CharField(max_length =60)
    email = models.EmailField()
    userType = models.CharField(max_length =60)
    status = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)
