from django.shortcuts import render
from .models import Student, Teacher
from .serializers import TeacherSerializer, StudentSerializer
from rest_framework import generics
from rest_framework.permissions import isAuthenticated

class StudentList(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class TeacherList(generics.ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
