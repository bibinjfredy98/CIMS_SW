from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from GTRE_APPLICATION.models import MainAdmin

class Command(BaseCommand):
    help = 'Create a main admin user'

    def handle(self, *args, **options):
        username = input("Enter username for main admin: ")
        password = input("Enter password for main admin: ")

        user = User.objects.create_user(username=username, password=password)
        main_admin = MainAdmin.objects.create(user=user)

        self.stdout.write(self.style.SUCCESS(f"Main admin {username} created successfully"))
