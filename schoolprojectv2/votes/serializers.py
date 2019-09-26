from rest_framework import serializers
from .models import Vote
from django.contrib.contenttypes.models import ContentType


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('user', 'datestamp')

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    user_name = serializers.CharField(source='from_user', read_only=True)
    class Meta:
        model = Vote
        fields = ('user', 'user_name', 'datestamp')

    def validate(self, data):
        instance = self.context['instance']
        user = self.context['request'].user
        activity_type = "L"
        content_type = ContentType.objects.get_for_model(model=instance)
        object_id = instance.id
        #check that the actual instance is unique
        if Vote.objects.filter(
            user = user,
            activity_type = activity_type,
            content_type = content_type,
            object_id = object_id
        ).exists():
            raise serializers.ValidationError('The current User already liked that post')
        return data

    def create(self, validated_data):
        instance = self.context['instance']
        user = self.context['request'].user
        activity_type = "L"
        content_type = ContentType.objects.get_for_model(model=instance)
        object_id = instance.id
        like = Vote.objects.create(
            user = user,
            activity_type = activity_type,
            content_type = content_type,
            object_id = object_id
        )
        like.save()
        return like


class DownvoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    user_name = serializers.CharField(source='from_user', read_only=True)

    class Meta:
        model = Vote
        fields = ('user', 'user_name', 'datestamp')


    def validate(self, data):
        instance = self.context['instance']
        user = self.context['request'].user
        activity_type = "D"
        content_type = ContentType.objects.get_for_model(model=instance)
        object_id = instance.id
        #check that the actual instance is unique
        if Vote.objects.filter(
            user = user,
            activity_type = activity_type,
            content_type = content_type,
            object_id = object_id
        ).exists():
            raise serializers.ValidationError('The current User already downvoted that post')
        return data

    def create(self, validated_data):
        instance = self.context['instance']
        user = self.context['request'].user
        activity_type = "D"
        content_type = ContentType.objects.get_for_model(model=instance)
        object_id = instance.id
        like = Vote.objects.create(
            user = user,
            activity_type = activity_type,
            content_type = content_type,
            object_id = object_id
        )
        like.save()
        return like
