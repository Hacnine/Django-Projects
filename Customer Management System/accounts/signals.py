from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# from .models import Profile
from accounts.models import Customer


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customers')
        instance.groups.add(group)

        Customer.objects.create(user=instance, name=instance.username, email=instance.email)

        # Profile.objects.create(user=instance)
        print('Profile created!')


post_save.connect(create_profile, sender=User)
#
# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
#         print('Profile updated!')
#
#
# post_save.connect(update_profile, sender=User)
