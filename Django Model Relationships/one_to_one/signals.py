from django.db.models.signals import post_delete
from django.dispatch import receiver

from one_to_one.models import Page, PageThree


@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    print('Page Post_Delete')
    instance.user.delete()


@receiver(post_delete, sender=PageThree)
def delete_related_user(sender, instance, **kwargs):
    print('Page Post_Delete')
    instance.muser.delete()
