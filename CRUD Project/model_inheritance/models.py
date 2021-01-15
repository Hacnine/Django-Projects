from django.db import models


class InheritanceUser(models.Model):

    teacher_name = models.CharField(max_length=70)
    employee_name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
