from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

class Community(models.Model):
    PRIVACY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('restricted', 'Restricted'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='public')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='community_participants')
    participants_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
    def save(self, *args, **kwargs):
        if not self.pk and not self.user_id:  # Only set the user on creation
            self.user = get_user_model().objects.get(username='your_default_username_here')
        super().save(*args, **kwargs)
    