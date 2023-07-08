from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Assign staff permissions to the superuser account.'

    def handle(self, *args, **options):
        username = 'raem'
        try:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Staff permissions assigned to the superuser account.'))
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'Superuser account "{username}" does not exist.'))
