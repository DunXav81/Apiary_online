from django.apps import AppConfig


class ScalesApiaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scales_apiary'

    def ready(self):
        from . import crontab
        crontab.start()