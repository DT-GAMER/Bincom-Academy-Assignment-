from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from albums.models import Album
from django.conf import settings

class Memory(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='memories/videos/', null=True, blank=True)
    description = models.TextField()
    caption = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='memories/')
    video = models.FileField(upload_to='memories/videos/', null=True, blank=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owners_uploaded')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='memories_likes', blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaded_memories')
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name='commented_memories')

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('memory-detail', args=[str(self.id)])

class Comment(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_memories')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.memory.caption}'

