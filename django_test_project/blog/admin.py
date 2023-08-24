from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", "published_at")

    fields = ["title", "content", "author", "published_at"]

    ordering = ["-published_at"]
    list_filter = ["published_at"]

    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)