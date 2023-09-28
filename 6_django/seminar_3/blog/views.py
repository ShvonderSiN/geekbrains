from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Article, Author


def index(request: HttpRequest) -> render:
    context = {
        'title': 'Главная страница',
        'content': 'Чтобы выбрать автора, укажите в адресе его ID (author/id).'
    }
    authors = Author.objects.all()
    context['authors'] = authors
    return render(request, template_name='blog/index.html', context=context)


def articles_by_author(request: HttpRequest, author_pk: int) -> render:
    author = get_object_or_404(Author, pk=author_pk)
    articles = Article.objects.filter(author=author)
    context = {
        'title': f'Автор {author.full_name}',
        'articles': articles
    }
    return render(request, template_name='blog/articles_by_author.html', context=context)


def article_full(request: HttpRequest, article_pk: int) -> render:
    article = get_object_or_404(Article, pk=article_pk)
    article.views_count()
    comments = article.comments.select_related('author').all()
    print(article.comments)

    context = {
        'article': article,
        'comments': comments
    }
    return render(request, template_name='blog/article_full.html', context=context)
