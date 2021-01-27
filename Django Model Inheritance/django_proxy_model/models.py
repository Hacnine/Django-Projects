from django.db import models


class ExamCenterTwo(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)


class MyExamCenter(ExamCenterTwo):
    class Meta:
        proxy = True
        # ordering = ['-id']
        # ordering = ['city']
        ordering = ['-city']
