from datetime import datetime

from django.core.management.base import BaseCommand
from blog.models import Article, Author


class Command(BaseCommand):
    help = "Generate fake authors and articles."

    def add_arguments(self, parser):
        parser.add_argument('num', type=int, help='Num of authors')

    def handle(self, *args, **kwargs):
        num = kwargs.get('num', 10)
        for i in range(1, num + 1):
            author = Author.objects.create(
                name=f'Author{i}',
                surname=f'Surname{i}',
                email=f'{i}@mail.ru',
                biography=f'Biography{i}',
                birthday=datetime.strptime(f'01.01.{i:04}', '%d.%m.%Y')
            )
            author.save()
            for j in range(1, num + 1):
                article = Article.objects.create(
                    title=f'Title{j}',
                    content=f'Content{j}',
                    publication_date=datetime.today(),
                    author=author
                )
                article.save()
        self.stdout.write(f'Fake authors and articles created')
