from django.apps import AppConfig


class DenishIvySignalsConfig(AppConfig):
    name = 'denish_ivy_signals'

    def ready(self):
        import denish_ivy_signals.signals
