from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'content', "is_published")
    list_filter = ("name", "is_published")
    search_fields = ("name", 'content')
