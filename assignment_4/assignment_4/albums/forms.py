from django import forms
from .models import Album, Memory

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description']

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = []
