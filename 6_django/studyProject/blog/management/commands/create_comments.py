import random

from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Article, Author, Comment


class Command(BaseCommand):
    help = "Generate fake comments."

    def add_arguments(self, parser):
        parser.add_argument('num', type=int, help='Num of comments')

    def handle(self, *args, **kwargs):
        fake = Faker()
        num = kwargs.get('num', 10)
        all_articles = Article.objects.all()
        all_authors = Author.objects.all()
        for article in all_articles:
            for _ in range(num):
                Comment.objects.create(
                    author=random.choice(all_authors),
                    article=article,
                    comment=fake.text(),
                    created_at=fake.date_time_this_year(),
                    updated_at=fake.date_time_this_year()
                )

        self.stdout.write(f'{num} Fake comments created for each article.')
