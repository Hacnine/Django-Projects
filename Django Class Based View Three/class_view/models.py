from django.db import models
from django.urls import reverse


class ClassEmployee(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)

    # def get_absolute_url(self):
    #     return reverse('name-submit')

    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})