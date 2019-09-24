from django.urls import path, include
from .views import (
    PostList,
    PostDetail,
    MyPostList,
)


urlpatterns = [
    path('', PostList.as_view(), name="post-list"),
    path('<int:id>/', PostDetail.as_view(), name="post-detail"),
    path('myposts/', MyPostList.as_view(), name="post-myposts"),
]
