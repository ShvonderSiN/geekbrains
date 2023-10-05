from django.core.management.base import BaseCommand
from shop.models import Client, Good
from faker import Faker


class Command(BaseCommand):
    help = "Create new Good"

    def add_arguments(self, parser):
        faker = Faker(locale='ru-ru')
        parser.add_argument('--title', default=faker.text(max_nb_chars=50), type=str, help='Name of good')
        parser.add_argument('--descr', default=faker.text(max_nb_chars=400), type=str, help='Description')
        parser.add_argument('--q', default=faker.random_number(digits=3, fix_len=False), type=str, help='quantity')
        parser.add_argument('--price', default=faker.random_number(digits=8), type=str, help='Price')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        descr = kwargs.get('descr')
        q = kwargs.get('q')
        price = kwargs.get('price')

        new_good = Good.objects.create(
            title=title,
            description=descr,
            quantity=q,
            price=price,
        )
        self.stdout.write(f'Good {new_good.title} created')
