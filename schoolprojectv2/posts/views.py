from django.shortcuts import render
from .permissions import isAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [isAuthenticatedOrReadOnly]
