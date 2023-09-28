from django.urls import path
from .views import index, articles_by_author, article_full

urlpatterns = [
    path('', index, name='index'),
    path('author/<int:author_pk>', articles_by_author, name='articles_by_author'),
    path('article/<int:article_pk>', article_full, name='article_full'),
]
