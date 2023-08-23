from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User, Album, Memory, Comment

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile_picture', 'bio')

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'description')

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ('title', 'description', 'image', 'video', 'album')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
