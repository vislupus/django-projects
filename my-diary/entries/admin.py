from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "date_created")

    fields = ["title", "content", "date_created"]

    ordering = ["-date_created"]
    list_filter = ["date_created"]

    search_fields = ["title", "content"]


admin.site.register(Entry, EntryAdmin)
