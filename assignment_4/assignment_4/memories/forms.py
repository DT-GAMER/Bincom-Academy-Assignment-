from django import forms
from .models import Memory, Comment

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['title', 'description', 'image', 'video']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
