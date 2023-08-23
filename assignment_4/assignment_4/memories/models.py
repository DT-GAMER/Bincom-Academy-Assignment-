from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from albums.models import Album

class Memory(models.Model):
    caption = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='memories/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_memories', blank=True)
    comments = models.ManyToManyField(User, through='Comment', related_name='commented_memories')

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('memory-detail', args=[str(self.id)])

class Comment(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.memory.caption}'

