from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Creates superuser if it does not exist already'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(username=username).exists():
            self.stdout.write(f'Creating superuser {username}')
            User.objects.create_superuser(
                username=username, email=email, password=password
            )
        else:
            self.stdout.write(f'Superuser {username} already exists')
