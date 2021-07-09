from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Balance(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    asset = models.FloatField(default = 0.000)
    capital =  models.FloatField(default = 0.000)
    profit = models.FloatField(default = 0.000)
    btc =  models.FloatField(default = 0.000)
    usd =  models.FloatField(default = 0.000)
    
    def __str__(self):
        return str(self.name)
# Create your models here.
