from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import UserSerializer
from rest_auth.models import TokenModel

class TokenSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = TokenModel
        fields = ('key', 'user')
