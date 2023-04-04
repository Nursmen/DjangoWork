from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):
    myself = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=8)