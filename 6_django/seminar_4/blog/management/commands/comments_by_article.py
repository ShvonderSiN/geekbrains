from django.core.management.base import BaseCommand
from blog.models import Article, Comment


class Command(BaseCommand):
    help = "Get all comments by article"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('--sort', type=str, default='id', help='Sorting by')
        parser.add_argument('--limit', type=int, default=5, help='Limit of comments')

    def handle(self, *args, **kwargs):
        global comments
        pk = kwargs.get('pk')
        sort = kwargs.get('sort')
        limit = kwargs.get('limit')
        if pk:
            article = Article.objects.filter(pk=pk).first()
            comments = Comment.objects.filter(article=article).order_by(sort)[:limit]

            self.stdout.write(f'Комментарии к статье: {comments[0].article}')
            for comment in comments[:5]:
                self.stdout.write(f'{comment.comment}')
        else:
            return 'Такой статьи нет'
