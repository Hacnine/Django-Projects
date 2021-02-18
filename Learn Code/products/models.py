from django.db import models
from django.db.models.signals import post_save


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()

    def __str__(self):
        return self.name

