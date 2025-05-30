from django.apps.config import AppConfig


class ParserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boss_test.apps.parser'
    label = 'parser'