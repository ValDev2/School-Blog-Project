from rest_framework import serializers
from .models import Comment
from django.contrib.contenttypes.models import ContentType


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="email", read_only=True)
    class Meta:
        model = Comment
        fields = ('id','user', 'user_name', 'content', 'is_parent', 'datestamp')

class CommentParentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True, source="user.email")
    children_comments = serializers.SerializerMethodField()

    def get_children_comments(self, obj):
        return CommentChildSerializer(obj.get_children(), many=True).data

    class Meta:
        model = Comment
        fields = ('user', 'user_name', 'content', 'is_parent', 'children_comments')

class CommentChildSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True, source="user.email")

    class Meta:
        model = Comment
        fields = ('user', 'user_name', 'content', 'is_parent', 'object_id')


class CreateCommentSerializer(serializers.ModelSerializer):
    object_id = serializers.SerializerMethodField()
    user_name = serializers.CharField(source="user.email", read_only=True)

    def get_object_id(self, obj):
        return self.context['instance'].id

    #Check if the content's field is not empty
    def validate(self, data):
        if not('content' in list(data)):
            raise serializers.ValidationError("Please add content ...")
        return data

    def create(self, validated_data):
        instance = self.context['instance']
        object_id = instance.pk
        user = instance.user
        content = validated_data.get('content')
        content_type = ContentType.objects.get_for_model(model=instance)
        comment = Comment.objects.create(
            user = user,
            content_type = content_type,
            content = content,
            object_id = object_id
        )
        comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ('id','user_name', 'content', 'is_parent', 'object_id')
