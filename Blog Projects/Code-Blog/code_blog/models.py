from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200,)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000)

    def get_absolute_url(self):
        # return reverse('article', args=(str(self.id)))
        return reverse('home')