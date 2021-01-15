from django.db import models


class Categories(models.Model):
    shirt = models.CharField(max_length=10)
    tShit = models.CharField(max_length=255)
    fruits = models.CharField(max_length=10)
