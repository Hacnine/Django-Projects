from django.contrib.auth.models import User
from django.db import models


class Page(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True, limit_choices_to={'is_staff': True})

    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


class Like(Page):
    likes = models.IntegerField()
    like_user = models.OneToOneField(Page, on_delete=models.CASCADE,
                                     primary_key=True, parent_link=True)


class PageThree(models.Model):
    muser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
