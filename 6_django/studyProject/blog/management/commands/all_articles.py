from django.core.management.base import BaseCommand
from blog.models import Article


class Command(BaseCommand):
    help = "Get all articles"

    def handle(self, *args, **kwargs):
        articles = Article.objects.all()
        for article in articles:
            self.stdout.write(f'{article.title}, Автор: {article.author.full_name}')
