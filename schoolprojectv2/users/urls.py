from .views import ( UserList,
                        UserDetail,
                        UserFriendRequest,
                        UserSentFriendRequest,
                        GetFriendRequest,
                        GetSentFriendRequest,
                        DeleteSentFriendRequest,
                        ExperienceList,

                    )
from django.urls import path, include

urlpatterns = [
    path('', UserList.as_view(), name="users-list"),
    path('profile/<int:pk>/', UserDetail.as_view(), name="user-detail"),
    path('profile/<int:pk>/experiences/', ExperienceList.as_view(), name="user-experiences"),
    path('profile/friendrequests/', UserFriendRequest.as_view(), name="user-friendrequest"),
    path('profile/friendrequests/<int:id>/', GetFriendRequest.as_view(), name="user-friendrequest-detail"),
    path('profile/friendrequests/sent/', UserSentFriendRequest.as_view(), name="user-friendrequest"),
    path('profile/friendrequests/sent/<int:id>/', GetSentFriendRequest.as_view(), name="user-sentfriendrequest"),
    path('profile/friendrequests/sent/<int:id>/delete', DeleteSentFriendRequest.as_view(), name="user-friendrequest-delete"),
]
