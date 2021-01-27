from django.db import models


class StudentTwo(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    admission_datetime = models.DateTimeField(default=True, null=True)
    pass_date = models.DateField()




