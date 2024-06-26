from django.db import models


# Create your models here.
class user_register(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()


class NotesClass(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='User_Notes')
    discription=models.TextField()


