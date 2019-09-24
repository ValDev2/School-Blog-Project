from django.shortcuts import render
from .permissions import isAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics

#Get all existing posts : Create new post / see all posts
class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [isAuthenticatedOrReadOnly]


#Get Post Details : delete / update / get the post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [isAuthenticatedOrReadOnly]

#Get my posts : List
class MyPostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [isAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(user = self.request.user)
