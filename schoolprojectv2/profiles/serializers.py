from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('grade', 'major', 'degree')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('completed_degree', 'researches')
