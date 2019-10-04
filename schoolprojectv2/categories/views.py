from django.shortcuts import render
from .serializers import CategoryTypeSerializer
from .models import CategoryType
from rest_framework import generics

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryTypeSerializer
    queryset = CategoryType.objects.all()
