from django.shortcuts import render
from .permissions import isAuthenticatedOrReadOnly, isAuthorOrReadOnly
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from votes.serializers import ActivitySerializer, LikeSerializer, DownvoteSerializer
from comments.serializers import CommentChildSerializer, CommentParentSerializer
from votes.models import Vote
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType


#Get all existing posts : Create new post / see all posts
class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [isAuthenticatedOrReadOnly]

#Get Post Details : delete / update / get the post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [isAuthenticatedOrReadOnly, isAuthorOrReadOnly]

#Get my posts : List
class MyPostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [isAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(user = self.request.user)

#Get all post's likes and able the user to like the post
class PostLikeDetail(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [isAuthenticatedOrReadOnly]
    #Tell the view what url parameter we are looking for
    lookup_url_kwargs = "pk"

    def get_queryset(self):
        #grab the value of this parameter
        pk = self.kwargs.get(self.lookup_url_kwargs)
        post = get_object_or_404(Post, pk=pk)
        content_type = ContentType.objects.get_for_model(model=post)
        print(f"pk = {pk}")
        return Vote.objects.filter(activity_type='L', object_id = pk, content_type=content_type)

    def get_serializer_context(self):
        id = self.kwargs.get(self.lookup_url_kwargs)
        qs = Post.objects.filter(id = id).first()
        return {'request': self.request, 'instance': qs}

#Destroy the like instance
class PostDestroyLike(generics.RetrieveDestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [isAuthenticatedOrReadOnly, isAuthorOrReadOnly]
    lookup_url_kwargs = "pk"

    #Return a qs of the post's likes
    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwargs)
        post = get_object_or_404(Post, pk=pk)
        content_type = ContentType.objects.get_for_model(model=post)
        return Vote.objects.likes().filter(content_type = content_type, object_id = pk)

    #get the actual post object
    def get_object(self):
        pk = self.kwargs.get(self.lookup_url_kwargs)
        obj = get_object_or_404(Vote, object_id=pk, user=self.request.user,  activity_type="L")
        return obj

#Get all downvotes and able the user to downvote a post
class PostDownVoteDetail(generics.ListCreateAPIView):
    serializer_class = DownvoteSerializer
    permission_classes = [isAuthenticatedOrReadOnly]
    lookup_url_kwargs = "pk"

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwargs)
        post = get_object_or_404(Post, pk=pk)
        content_type = ContentType.objects.get_for_model(model=post)
        return Vote.objects.downvotes().filter(content_type = content_type, object_id = pk)

    def get_serializer_context(self):
        id = self.kwargs.get(self.lookup_url_kwargs)
        qs = Post.objects.filter(id = id).first()
        return {'request': self.request, 'instance': qs}

#Get the user's downvote of a post and destroy it
class PostDestroyDownvote(generics.RetrieveDestroyAPIView):
    serializer_class = DownvoteSerializer
    permission_classes = [isAuthenticatedOrReadOnly]
    lookup_url_kwargs = "pk"

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwargs)
        post = get_object_or_404(Post, pk=pk)
        content_type = ContentType.objects.get_for_model(model=post)
        print(content_type)
        return Vote.objects.downvotes().filter(content_type = content_type, object_id=pk)

    def get_object(self):
        pk = self.kwargs.get(self.lookup_url_kwargs)
        obj = get_object_or_404(Post, pk = pk)
        print(obj)
        return obj
