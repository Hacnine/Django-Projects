from django.apps import AppConfig


class CustomSignalsConfig(AppConfig):
    name = 'custom_signals'
    #
    # def ready(self):
    #     import custom_signals.signals
