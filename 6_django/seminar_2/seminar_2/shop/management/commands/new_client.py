from django.core.management.base import BaseCommand
from shop.models import Client
from faker import Faker


class Command(BaseCommand):
    help = "Create new client"

    def add_arguments(self, parser):
        faker = Faker('ru-ru')
        parser.add_argument('--name', default=faker.name(), type=str, help='Name of client')
        parser.add_argument('--email', default=faker.email(), type=str, help='Email')
        parser.add_argument('--phone', default=faker.phone_number(), type=str, help='Phone')
        parser.add_argument('--address', default=faker.address(), type=str, help='Phone')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        new_client = Client.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        self.stdout.write(f'Client {new_client.name} created')

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
