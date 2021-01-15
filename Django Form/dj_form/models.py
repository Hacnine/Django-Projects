from django.db import models


class Employee(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    subject = models.TextField(max_length=200)
