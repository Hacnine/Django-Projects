from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, post_init, pre_init
from django.dispatch import receiver
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.cache import cache_page


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    # print("logged in signal ................")
    # print("Sender", sender)
    # print('Request:', request)
    # print("User", user)
    # print("User Name", user.username)
    # print(f'Kwargs: {kwargs}')'
    pass


# user_logged_in.connect(login_success, sender=User)  # or use @receiver


@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    # print("logged out signal ................")
    # print("Sender", sender)
    # print('Request:', request)
    # print("User", user)
    # print("User Name", user.username)
    # print(f'Kwargs: {kwargs}')
    pass


# user_logged_out.connect(logout_success, sender=User)  # or use @receiver


@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    # print("login failed signal ................")
    # print("Sender", sender)
    # print('Request:', request)
    #
    # print("Credentials", credentials)
    # print("kwargs", kwargs)
    # return HttpResponse('You have tried maximum')
    pass




@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    # print("at_beginning_save ................")
    # print("Sender", sender)
    # print('Instance:', instance)
    # print(f'Kwargs: {kwargs}')
    pass


# @cache_page(30)
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    # if created:
    #     print("New user created")
    #     print('Created:', created)
    #     print("Sender", sender)
    #     print('Instance:', instance)
    #     print(f'Kwargs: {kwargs}')
    # else:
    #     print('User information updated.')
    pass


@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    # print("at_beginning_delete ................")
    # print("Sender", sender)
    # print('Instance:', instance)
    # print(f'Kwargs: {kwargs}')
    pass


@receiver(post_delete, sender=User)
def at_end_delete(sender, instance, **kwargs):
    # print("at_end_delete ................")
    # print("Sender", sender)
    # print('Instance:', instance)
    # print(f'Kwargs: {kwargs}')
    pass


@receiver(pre_init, sender=User)
def at_begging_init(sender, *args, **kwargs):
    # print("at_begging_init ................")
    # print("Sender", sender)
    # print('*args:', *args)
    # print(f'Kwargs: {kwargs}')
    pass


@receiver(post_init, sender=User)
def at_end_init(sender, *args, **kwargs):
    # print("at_end_init ................")
    # print("Sender", sender)
    # print('args:', args)
    # print(f'Kwargs: {kwargs}')
    pass


@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    # print("at_request_exception ................")
    # print("Sender", sender)
    # print('request', request)
    # print(f'Kwargs: {kwargs}')
    pass


@receiver(connection_created)
def connect_db(sender, connection, **kwargs):
    # print("connect_db ................")
    # print("Sender", sender)
    # print('connection', connection)
    # print(f'Kwargs: {kwargs}')
    pass