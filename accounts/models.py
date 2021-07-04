from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class balance(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    balance = models.IntegerField(default = 0)