from django.apps.config import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boss_test.apps.core'
    label = 'core'