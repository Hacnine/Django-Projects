from django.apps import AppConfig


class DjangoCookiesConfig(AppConfig):
    name = 'one_to_one'

    def ready(self):
        import one_to_one.signals