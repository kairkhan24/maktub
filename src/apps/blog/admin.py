from django.contrib import admin

from apps.blog.models import (
    Category,
    Source,
    Author,
    Tag,
    Post,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    search_fields = ('title',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title', 'url')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'source', 'category')
    search_fields = (
        'title', 'author__name', 'category__title',
        'source_title', 'description', 'slug'
    )
    list_filter = ('category', 'author', 'source')
    readonly_fields = ('viewed',)
