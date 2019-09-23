from rest_framework import serializers
from votes.serializers import ActivitySerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    likes = serializers.SerializerMethodField()
    like_number = serializers.SerializerMethodField()
    downvotes_number = serializers.SerializerMethodField()

    def create(self, validated_data):
        if self.is_valid():
            post = Post.objects.create(
                user = self.context['request'].user,
                title = self.validated_data['title'],
                content = self.validated_data['content'],
                tags = self.validated_data['tags']
            )
            post.save()
            return post

    def get_likes(self, obj):
        return ActivitySerializer(obj.activities.filter(activity_type='L'), many=True).data

    def get_downvotes_number(self, obj):
        return obj.activities.filter(activity_type='D').count()

    def get_like_number(self, obj):
        return obj.activities.filter(activity_type='L').count()

    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'tags', 'like_number', 'downvotes_number', 'likes')
