from django.contrib.auth.models import User
from django.db import models


class PostTwo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# primary_key=True, limit_choices_to={'is_staff': True}
    post_title = models.CharField(max_length=70)
    page_category = models.CharField(max_length=70)
    page_publish_date = models.DateField()
