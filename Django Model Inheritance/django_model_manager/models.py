from django.db import models

from django_model_manager.managers import CustomManager


class StudentModel(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # objects = models.Manager()
    # custom_manager = models.Manager()
    # custom_manager = CustomManager()


class ProxyStudentModel(StudentModel):
    custom_manager = CustomManager()

    class Meta:
        proxy = True
