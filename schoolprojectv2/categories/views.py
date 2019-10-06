from django.shortcuts import render
from .serializers import CategoryTypeSerializer, CategoryFieldSerializer
from .models import CategoryType
from rest_framework import generics

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryTypeSerializer
    queryset = CategoryType.objects.all()

class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategoryTypeSerializer
    lookup_field = "slug"
    lookup_url_kwargs = "slug"
    queryset = CategoryType.objects.all()
