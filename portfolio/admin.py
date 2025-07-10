from django.contrib import admin
from django.contrib.admin import register
from portfolio import models

# Register your models here.
@register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    search_fields = ('name', 'description',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'article', 'created_at',)
    search_fields = ('content',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('name',)

