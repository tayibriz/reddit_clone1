from django.db import models
from django.conf import settings
from django.utils import timezone
from community.models import Community
from django.contrib.auth import get_user_model

class Post(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    community_image_url = models.URLField(blank=True, null=True)  # URL for the community image
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edited_at = models.DateTimeField(blank=True, null=True)
    number_of_comments = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200)
    VOTE_CHOICES = [
        ('upvote', 'Upvote'),
        ('downvote', 'Downvote'),
        ('neutral', 'Neutral'),
    ]
    vote_status = models.CharField(max_length=10, choices=VOTE_CHOICES, default='neutral')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and not self.creator_id:
            self.creator = get_user_model().objects.get(username='your_default_username_here')
        super().save(*args, **kwargs)