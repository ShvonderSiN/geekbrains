from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "автора"
        verbose_name_plural = "авторы"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статьи")
    content = models.TextField(verbose_name="Текст статьи")
    publication_date = models.DateField(verbose_name="Дата публикации")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name="Автор",
    )
    category = models.CharField(max_length=100, verbose_name="Категория")
    views = models.IntegerField(default=0, verbose_name="Количество просмотров")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def views_count(self) -> None:
        """Увеличивает количество просмотров на 1"""
        self.views += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статью"
        verbose_name_plural = "статьи"


class Comment(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="comments"
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def updated(self):
        return self.updated_at != self.created_at

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
