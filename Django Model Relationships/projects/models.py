from django.contrib.auth.models import User
from django.db import models


class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True, limit_choices_to={'is_staff': True})

    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


class Work(models.Model):
    user = models.ManyToManyField(User)
    work_title = models.CharField(max_length=70)
    work_duration = models.IntegerField()

    def done_by(self):
        d_by = ', '.join([str(p) for p in self.user.all()])
        return d_by

