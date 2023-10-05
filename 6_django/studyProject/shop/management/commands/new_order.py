from _decimal import ROUND_DOWN
from django.core.management.base import BaseCommand
from shop.models import Client, Good, Order
from faker import Faker
from decimal import Decimal


class Command(BaseCommand):
    help = "Create new order"

    def add_arguments(self, parser):
        faker = Faker(locale='ru-ru')
        parser.add_argument('--client_id', default=1, type=int, help='Client ID')
        parser.add_argument('--good_id', default=1, type=int, help='Good ID')
        parser.add_argument('--quantity', default=3, type=int, help='Count of goods in order')

    def handle(self, *args, **kwargs):
        client_pk = kwargs.get('client_id')
        good_pk = kwargs.get('good_id')
        quantity = Decimal(kwargs.get('quantity'))
        client = Client.objects.filter(pk=client_pk).first()
        good = Good.objects.filter(pk=good_pk).first()
        total_price = self.__total_price(good=good, quantity=quantity)

        new_order = Order.objects.create(
            client=client,
            good=good,
            total=total_price,
        )
        self.stdout.write(f'Order {new_order.pk} created,  Total price {total_price}')

    def __total_price(self, good, quantity):
        total = good.price * quantity
        return total
