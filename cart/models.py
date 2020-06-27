from django.db import models

# Create your models here.
from products.models import Products
class Cart(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ManyToManyField(Products , blank=True  )

