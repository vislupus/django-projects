from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "date_created")

    fields = ["title", "content", "date_created"]

    ordering = ["-date_created"]
    list_filter = ["date_created"]

    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)