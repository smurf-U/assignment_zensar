import random
from faker import Faker
from django.core.management.base import BaseCommand
from test_zensar.models import RouterManager

class Command(BaseCommand):
    help = 'Populate data using Faker lib.'

    def _create_partner(self, activity):
        fake = Faker()
        router = RouterManager(
            sapid=fake.ssn(),
            hostname=fake.hostname(),
            loopback=fake.ipv4(), 
            mac_address=fake.mac_address(),
        )
        router.save()

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of partner to be created')


    def handle(self, *args, **kwargs):
        for i in range(kwargs['total']):
            self._create_partner(i)