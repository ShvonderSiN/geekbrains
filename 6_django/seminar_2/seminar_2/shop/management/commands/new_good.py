from django.core.management.base import BaseCommand
from shop.models import Client, Good
from faker import Faker


class Command(BaseCommand):
    help = "Create new client"

    def add_arguments(self, parser):
        faker = Faker(locale='ru-ru')
        parser.add_argument('--title', default=faker.text(max_nb_chars=50), type=str, help='Name of client')
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

# 1,Client-1,dwilcox@example.net,+1-619-235-6305x92220,"6840 Reynolds Tunnel Apt. 994
# Lake Williamfurt, MA 22955",2023-09-24 17:19:04.877701
# 2,Monica Hawkins,stephaniescott@example.org,361.688.5076x4481,"158 Janice River Suite 088
# Cervantesbury, TN 38524",2023-09-24 17:19:46.904998
# 3,Michael Clark,heather37@example.net,605.435.5908x7972,"6776 Sarah Mountain Suite 239
# Jenkinsland, DE 44871",2023-09-24 17:19:51.179131
# 4,Samantha Hodge,marcus28@example.org,(727)203-3472,"43580 Gina Prairie
# South Maryburgh, NY 66287",2023-09-24 17:19:53.098316
# 5,Robert Cameron,annettechandler@example.org,957.628.2512x87040,"92743 Austin Lodge
# Port Ashleyborough, GA 67282",2023-09-24 17:19:55.229585
