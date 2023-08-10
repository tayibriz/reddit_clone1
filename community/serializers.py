from rest_framework import serializers
from .models import Community
class CommunitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    participants_count = serializers.ReadOnlyField()
    class Meta:
        model = Community
        fields = ['user', 'text', 'privacy', 'participants_count']
    