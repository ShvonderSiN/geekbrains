from django.contrib import admin
from .models import Article, Author, Comment


@admin.action(description="Опубликовать")
def publish_all_articles(modeladmin, request, queryset):
    queryset.update(is_published=True)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "content",
        ("publication_date", "author", "category"),
        "is_published",
    )
    list_display = ("pk", "title", "author", "category", "is_published", "views")
    list_display_links = ("title",)
    list_editable = ("is_published",)
    readonly_fields = ("publication_date", "views")
    ordering = ("-pk", "title", "is_published", "-views")
    actions = (publish_all_articles,)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = (("name", "surname"), "email", "biography", "birthday")
    list_display = ("pk", "name", "surname", "email", "birthday")
    list_display_links = ("name", "surname")
    ordering = ("-pk", "name", "surname")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ("author", "article", "comment", ("created_at", "updated_at"))
    list_display = ("pk", "author", "article", "created_at", "updated_at")
    list_display_links = ("pk", "author", "article")
    ordering = ("-pk", "author", "article")
    readonly_fields = ("created_at", "updated_at")
