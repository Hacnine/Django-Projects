from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    fees = models.IntegerField()
    date = None


class Teacher(CommonInfo):
    date = models.DateField()
    salary = models.IntegerField(null=False)


class Constructor(CommonInfo):
    payment = models.IntegerField()
