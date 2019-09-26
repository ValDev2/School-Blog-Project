from rest_framework import serializers
from .models import Comment

class CommentParentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True, source="user.email")
    class Meta:
        model = Comment
        fields = ('user', 'user_name', 'content', 'is_parent')

class CommentChildSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True, source="user.email")
    class Meta:
        model = Comment
        fields = ('user', 'user_name', 'content', 'is_parent')
