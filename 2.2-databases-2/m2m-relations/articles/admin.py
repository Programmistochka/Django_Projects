from django.contrib import admin

from .models import Article, Tag, Scope

class ScopesInline(admin.TabularInline):
    model = Scope

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ScopesInline]
