from rest_framework import serializers
from .models import Vote

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('user', 'datestamp')
