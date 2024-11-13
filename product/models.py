from django.db import models
from shop.models import Shop


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.CharField(max_length=250)
