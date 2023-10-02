from datetime import datetime

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Article, Author


class Command(BaseCommand):
    help = "Update single article"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Article ID')
        parser.add_argument('name', type=str, help='New title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        if pk and name:
            article = Article.objects.filter(pk=pk).first()
            if article is not None:
                article.title = name
                article.save()
                self.stdout.write(f'{article.title} updated')
            else:
                self.stdout.write(f'Article with pk={pk} does not exist')
        else:
            self.stdout.write('Enter valid data, nothing to update')
