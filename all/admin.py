from django.contrib import admin
from all.models import Article, Category

# Register your models here.
@admin.register(Category)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)

@admin.register(Article)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category_name',)