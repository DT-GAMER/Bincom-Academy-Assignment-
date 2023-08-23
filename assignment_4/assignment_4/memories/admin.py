from django.contrib import admin
from .models import Memory

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('caption', 'album', 'uploaded_by', 'upload_date')
    list_filter = ('album', 'upload_date')
    search_fields = ('caption', 'album__title', 'uploaded_by__username')

