from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Snipbox, Tag

@admin.register(Snipbox)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'user')
    search_fields = ('title', 'note')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

