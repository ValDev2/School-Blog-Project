from django.urls import path, include
from .views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name="category-list")
]
