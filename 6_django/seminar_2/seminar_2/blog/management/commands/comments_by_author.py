from django.core.management.base import BaseCommand
from blog.models import Author, Comment


class Command(BaseCommand):
    help = "Get all comments by Author"

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
            author = Author.objects.filter(pk=pk).first()
            comments = Comment.objects.filter(author=author).order_by(sort)[:limit]

            self.stdout.write(f'Автор: {comments[0].author.full_name}')
            for comment in comments:
                self.stdout.write(f'{comment.comment}')
        else:
            return 'Такого автора нет'
