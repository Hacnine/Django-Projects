from django.dispatch import Signal, receiver

notification = Signal(providing_args=['request', 'user'])


@receiver(notification)
def show_notification(sender, **kwargs):
    print('Sender: ', sender)
