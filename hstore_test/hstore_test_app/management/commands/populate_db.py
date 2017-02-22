from django.core.management.base import BaseCommand

from hstore_test_app.populate_db import populate_db


class Command(BaseCommand):

    def handle(self, *args, **options):
        populate_db()
