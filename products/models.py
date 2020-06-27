from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100 , null=True , blank=True)
    price = models.IntegerField(default=100)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name