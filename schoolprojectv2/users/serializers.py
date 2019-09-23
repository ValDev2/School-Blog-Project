from rest_framework import serializers
from .models import FriendRequest, Experience
from profiles.serializers import StudentSerializer, TeacherSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    user_profile = serializers.SerializerMethodField()
    experiences = serializers.SerializerMethodField()
    user_status = serializers.SerializerMethodField()

    def get_followers(self, obj):
        frdrqst = obj.get_friendrequest()
        followers = [rsqt.from_user for rsqt in frdrqst]
        return UserFollowSerializer(followers, many=True).data

    def get_following(self, obj):
        frdrqst = obj.get_sent_friendrequest()
        following = [rqst.to_user for rqst in frdrqst]
        return UserFollowSerializer(following, many=True).data

    def get_user_profile(self, obj):
        if hasattr(obj, 'student'):
            profile = obj.student
            return StudentSerializer(profile).data
        elif hasattr(obj, 'teacher'):
            profile = obj.teacher
            return TeacherSerializer(profile).data
        else:
            return None

    def get_experiences(self, obj):
        qs = Experience.objects.filter(user=obj)
        return ExperienceSerializer(qs, many=True).data

    def get_user_status(self, obj):
        if obj.is_student == None:
            return None
        elif obj.is_student:
            return "Student"
        else:
            return "Teacher"

    class Meta:
        model = User
        fields = ('id', 'email', 'admin', 'interests', 'followers', 'following', 'school', 'is_student', 'user_profile', 'experiences', 'user_status')



#Aimed to display infos about users from the follow or followers list
class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'bio')

class FriendRequestSerializer(serializers.ModelSerializer):

    from_user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())


    class Meta:
        model = FriendRequest
        fields = ('id', 'from_user', 'to_user', 'datestamp')


    def validate(self, data):
        print(data)
        #check if the from_user field is equal to the actual user
        if self.context['request'].user == data['to_user']:
            raise serializers.ValidationError("l'émetteur et le destinataire doivent être différent")
        return data

    def create(self, validated_data):
        #Automaticaly setting the owner of the request to the actual user when creating an instance of FriendRequest
        to_user = validated_data['to_user']
        if self.is_valid():
            request =  FriendRequest.objects.get_or_create(
                from_user = self.context['request'].user,
                to_user = to_user
            )
            if request[1]:
                return request[0]
            else:
                raise serializers.ValidationError('This instance already exists ! ')


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = "__all__"
