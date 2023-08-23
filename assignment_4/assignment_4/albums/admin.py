from django.contrib import admin
from .models import Album, Memory

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('owner', 'created_at', 'updated_at')

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('caption', 'album', 'created_at', 'updated_at')
    search_fields = ('caption',)
    list_filter = ('album', 'created_at', 'updated_at')

