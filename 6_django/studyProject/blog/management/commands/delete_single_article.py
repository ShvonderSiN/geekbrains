from datetime import datetime

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Article, Author


class Command(BaseCommand):
    help = "Delete single article"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            article = Article.objects.filter(pk=pk).first()
            if article is not None:
                article.delete()
                self.stdout.write(f'{article.title} deleted')
            else:
                self.stdout.write(f'Article with pk={pk} does not exist')
        else:
            self.stdout.write('Enter valid data, nothing to update')
