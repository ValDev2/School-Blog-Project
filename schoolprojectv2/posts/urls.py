from django.urls import path, include
from .views import (
    PostList,
    PostDetail,
    MyPostList,
    PostLikeDetail,
    PostDestroyLike,
    PostDownVoteDetail,
    PostDestroyDownvote,
    PostCommentList,
    PostCommentDetail,
)

urlpatterns = [
    path('', PostList.as_view(), name="post-list"),
    path('<str:slug>/', PostDetail.as_view(), name="post-detail"),
    #path('<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path('<int:pk>/likes/', PostLikeDetail.as_view(), name="post-likes"),
    path('<int:pk>/likes/destroy/', PostDestroyLike.as_view(), name="post-destroy-like"),
    path('<int:pk>/downvotes/', PostDownVoteDetail.as_view(), name="post-downvotes"),
    path('<int:pk>/downvotes/destroy/', PostDestroyDownvote.as_view(), name="post-destroy-downvote"),
    path('<int:pk>/comments/', PostCommentList.as_view(), name="post-comments"),
    path('<int:pk>/comments/<int:comment_id>/', PostCommentDetail.as_view(), name="post-comment-details"),
    path('myposts/', MyPostList.as_view(), name="post-myposts"),
]
