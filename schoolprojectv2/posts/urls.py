from django.urls import path, include
from .views import (
    PostList,
    PostDetail,
    MyPostList,
    PostLikeDetail,
    PostDestroyLike,
    PostDownVoteDetail,
    PostDestroyDownvote,
)


urlpatterns = [
    path('', PostList.as_view(), name="post-list"),
    path('<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path('<int:pk>/likes/', PostLikeDetail.as_view(), name="post-likes"),
    path('<int:pk>/likes/destroy/', PostDestroyLike.as_view(), name="post-destroy-like"),
    path('<int:pk>/downvotes/', PostDownVoteDetail.as_view(), name="post-downvotes"),
    path('<int:pk>/downvotes/destroy/', PostDestroyDownvote.as_view(), name="post-destroy-downvote"),
    path('myposts/', MyPostList.as_view(), name="post-myposts"),


]
