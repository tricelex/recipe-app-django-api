"""Django command to wait for DB to be available"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for database...')
        dp_up = False
        while not dp_up:
            try:
                self.check(databases=['default'])
                dp_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
