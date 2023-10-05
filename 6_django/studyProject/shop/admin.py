from django.contrib import admin
from django.utils.html import format_html

from .models import Client, Good, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "email",
        ("phone", "address"),
        "date",
    )
    list_display = ("pk", "name", "email", "phone", "address", "date")
    list_display_links = ("pk", "name")
    list_editable = ("phone",)
    readonly_fields = ("date",)
    ordering = ("-pk", "name", "email", "phone", "address", "date")
    list_per_page = 10


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "description",
        ("price", "quantity"),
        "date",
        ("image", "image_preview"),
    )
    list_display = ("pk", "title", "price", "quantity", "date", "image_preview")
    list_display_links = ("pk", "title")
    list_editable = ("price", "quantity")
    ordering = ("-pk", "title", "price", "quantity", "date")
    readonly_fields = ("date", "image_preview")

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No image"

    image_preview.short_description = "Image Preview"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = (
        "client",
        ("goods", "total"),
        "date",
        "date_edit",
    )
    list_display = ("pk", "client", "total", "date", "date_edit")
    list_display_links = ("date", "client")
    list_editable = ("total",)
    readonly_fields = ("date", "date_edit")
    ordering = ("-pk", "client", "total", "date", "date_edit", "total")
    filter = ("total", "date", "client")
