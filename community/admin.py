from django.contrib import admin
from .models import Community

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'get_privacy_display', 'created_at', 'participants_list')

    def participants_list(self, obj):
        return ', '.join([user.username for user in obj.participants.all()])

admin.site.register(Community, CommunityAdmin)