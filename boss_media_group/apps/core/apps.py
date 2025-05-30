from django.apps.config import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boss_media_group.apps.core'
    label = 'core'