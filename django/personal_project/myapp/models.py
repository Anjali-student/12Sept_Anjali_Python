from django.db import models

# Create your models here.
class userSignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=20)
    username = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=20)
