from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    # Fields from AbstractUser
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_age(self):
        from datetime import date
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    def has_profile_picture(self):
        return self.profile_picture is not None
    
    def is_complete_profile(self):
        return self.birth_date and self.location and self.website
    
    def send_welcome_email(self):
        subject = 'Welcome to MemoriesGallery'
        message = f'Hello {self.username},\n\nWelcome to MemoriesGallery! We are excited to have you as a part of our community.'
        from_email = 'your@email.com'  # Use your actual email address
        recipient_list = [self.email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return True
        except Exception as e:
            print(e)
            return False
