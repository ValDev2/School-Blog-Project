from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import UserSerializer, FriendRequestSerializer, ExperienceSerializer
from rest_framework.response import Response
from .models import User, FriendRequest, Experience
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permissions import (isOwner, isTarget, isCurrentUser)

#User List view that get all users
class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

#User Detail View that get details from a user Instance based on the id/pk
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, isCurrentUser]

#get all friendRequests sent by the OTHER users
class UserFriendRequest(generics.ListCreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [isTarget]
    def get_queryset(self):
        qs = FriendRequest.objects.filter(to_user = self.request.user)
        return qs

#get all friendsrequests made by the ACTUAL user
class UserSentFriendRequest(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = FriendRequest.objects.filter(from_user = self.request.user)
        return qs

#get/delete  a friendrequest Instance that a user recieved
class GetFriendRequest(generics.RetrieveDestroyAPIView):
    serializer_class = FriendRequestSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, isTarget]
    queryset = FriendRequest.objects.all()

#Delete a Friend request, which leads to unfollow a user
class DeleteSentFriendRequest(generics.DestroyAPIView):
    serializer_class = FriendRequestSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, isOwner]
    queryset = FriendRequest.objects.all()

#get/delete a friendrequest instance that a user sent !
class GetSentFriendRequest(generics.RetrieveDestroyAPIView):
    serializer_class = FriendRequestSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, isOwner]
    queryset = FriendRequest.objects.all()


#Create/Get the list of a user's experiences
class ExperienceList(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    def get_queryset(self):
        qs = Experience.objects.filter(user=self.request.user)
