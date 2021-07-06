from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Balance(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default = 0)
    
    def __str__(self):
        return str(self.name)
# Create your models here.
