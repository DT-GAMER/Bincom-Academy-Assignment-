from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

    def get_full_name(self):
        """
        Get the user's full name.
        """
        return f"{self.first_name} {self.last_name}"

    def get_liked_memories(self):
        """
        Get a list of memories liked by the user.
        """
        return self.liked_memories.all()

    class Meta:
        db_table = 'custom_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Provide unique related_name values to avoid clashes
    groups_related = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_groups',
    )

    user_permissions_related = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users_permissions',
    )

    user_permissions_related = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users_permissions',
        related_query_name='user',
    )

class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_memory_count(self):
        """
        Get the count of memories in the album.
        """
        return self.memory_set.count()

    def get_recent_memories(self, count=5):
        """
        Get a list of the most recent memories in the album.
        """
        return self.memory_set.order_by('-created_at')[:count]

class Memory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='memories/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='memories')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='liked_memories', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def is_liked_by_user(self, user):
        """
        Check if the memory is liked by a specific user.
        """
        return self.likes.filter(id=user.id).exists()

    def get_comment_count(self):
        """
        Get the count of comments on the memory.
        """
        return self.comments.count()

    def get_like_count(self):
        """
        Get the count of likes on the memory.
        """
        return self.likes.count()

    def add_comment(self, user, text):
        """
        Add a comment to the memory.
        """
        return self.comments.create(user=user, text=text)

    def toggle_like(self, user):
        """
        Toggle the like status of the memory for a specific user.
        """
        if self.likes.filter(id=user.id).exists():
            self.likes.remove(user)
        else:
            self.likes.add(user)

class Comment(models.Model):
    text = models.TextField()
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.memory.title}"

    def get_comment_count(self):
        """
        Get the count of comments on the memory.
        """
        return self.comments.count()

    def get_username(self):
        """
        Get the username of the user who posted the comment.
        """
        return self.user.username

    def is_owner(self, user):
        """
        Check if the comment was posted by a specific user.
        """
        return self.user == user


    

