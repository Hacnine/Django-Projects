from django.db import models


class User(models.Model):
    name = models.CharField(max_length=70, blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
