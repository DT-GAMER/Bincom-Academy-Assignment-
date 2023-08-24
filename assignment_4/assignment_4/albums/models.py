from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Album(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='albums_owned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Memory(models.Model):
    caption = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='memories_upload')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_albums', blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='memories')  # Use 'memories' here
    image = models.ImageField(upload_to='memories/')
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owners_upload')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption
