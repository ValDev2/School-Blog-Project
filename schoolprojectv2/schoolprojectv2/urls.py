from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views



urlpatterns = [
    path('', include('FrontEnd.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('posts/', include('posts.urls')),
    path('categories/', include('categories.urls')),
    path('rest-auth/', include('rest_auth.urls'), name="authentication"),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
