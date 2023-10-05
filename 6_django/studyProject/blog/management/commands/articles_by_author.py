from django.core.management.base import BaseCommand
from blog.models import Article, Author


class Command(BaseCommand):
    help = "Get all articles by Author"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('--sort', type=str, default='id', help='Sorting by')
        parser.add_argument('--limit', type=int, default=5, help='Limit of articles')

    def handle(self, *args, **kwargs):
        global articles
        pk = kwargs.get('pk')
        sort = kwargs.get('sort')
        limit = kwargs.get('limit')
        if pk:
            author = Author.objects.filter(pk=pk).first()
            articles = Article.objects.filter(author=author).order_by(sort)[:limit]

            self.stdout.write(f'Автор: {articles[0].author.full_name}')
            for article in articles:
                self.stdout.write(f'{article.title}')
        else:
            return 'Такого автора нет'
