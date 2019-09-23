from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class isAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated
