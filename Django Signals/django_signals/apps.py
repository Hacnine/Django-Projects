from django.apps import AppConfig


class DjangoCookiesConfig(AppConfig):
    name = 'django_signals'

    def ready(self):
        import django_signals.signals