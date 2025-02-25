from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a superuser account'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'nick@gmail.com', '1234')
            User.objects.create_superuser('hr_admin', 'hr_admin@gmail.com', 'hradmin2025')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
