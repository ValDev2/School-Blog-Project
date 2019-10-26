from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class isAuthenticatedOrReadOnly(BasePermission):

    message = "You must be Log In ! "

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

class isAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj)
        if request.method in SAFE_METHODS:
            return True
        #If the user is not the author, deny access to put / delete / post
        return obj.user == request.user
