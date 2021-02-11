from django.apps import AppConfig


class DjangoCookiesConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
