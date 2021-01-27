from django.contrib.auth.models import User
from django.db import models


class Work(models.Model):
    user = models.ManyToManyField(User)
    work_title = models.CharField(max_length=70)
    work_duration = models.IntegerField()

    def done_by(self):
        d_by = ', '.join([str(p) for p in self.user.all()])
        return d_by

