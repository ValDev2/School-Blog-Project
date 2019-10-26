from rest_framework import serializers
from votes.serializers import ActivitySerializer, LikeSerializer, DownvoteSerializer
from comments.models import Comment
from comments.serializers import CommentChildSerializer, CommentParentSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    user_name = serializers.CharField(source="get_username", read_only=True)
    likes = serializers.SerializerMethodField()
    like_number = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()
    downvotes_number = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comments_number = serializers.SerializerMethodField()
    category_field = serializers.CharField(source="category_type", read_only=True)
    category_subfield = serializers.CharField(source="category_name", read_only=True)

    def create(self, validated_data):
        if self.is_valid():
            post = Post.objects.create(
                user = self.context['request'].user,
                title = self.validated_data['title'],
                content = self.validated_data['content'],
                category = self.validated_data['category']
            )
            post.save()
            return post

    def get_likes(self, obj):
        return LikeSerializer(obj.activities.likes(), many=True).data

    def get_like_number(self, obj):
        return obj.activities.likes().count()

    def get_downvotes(self, obj):
        return DownvoteSerializer(obj.activities.downvotes(), many=True).data

    def get_downvotes_number(self, obj):
        return obj.activities.downvotes().count()

    def get_comments(self, obj):
        qs = Comment.objects.filter_by_instance(instance=obj)
        return CommentParentSerializer(qs, many=True).data

    def get_comments_number(self, obj):
        return obj.comments.filter_by_instance(instance=obj).count()


    class Meta:
        model = Post
        fields = ('id','user', 'user_name','title','slug', 'content', 'like_number', 'likes', 'downvotes', 'downvotes_number', 'comments', 'comments_number', 'category_field', 'category_subfield', 'category' )
