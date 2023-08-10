from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'community', 'creator_username', 'created_at', 'number_of_comments', 'vote_status')

    def creator_username(self, obj):
        return obj.creator.username

admin.site.register(Post, PostAdmin)
