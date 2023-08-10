from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Post
        fields = '__all__'