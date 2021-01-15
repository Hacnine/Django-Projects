from django.contrib.auth import user_logged_in
from django.contrib.auth.models import User
from django.core.cache import cache
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    # for track ip
    ip = request.META.get('REMOTE_ADDR')
    print('Ip', ip)
    request.session['ip'] = ip


@receiver(user_logged_in, sender=User)
def login_count(sender, request, user, **kwargs):
    log_count = cache.get('count', 0, version=user.pk)
    new_count = log_count + 1
    cache.set('count', new_count, 60*60*24, version=user.pk)