from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'tsm.core'

    def ready(self):
        import tsm.core.signals  # noqa
