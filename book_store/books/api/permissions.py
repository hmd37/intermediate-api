from rest_framework import permissions


class IsAdminOrStaffReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser or request.user.is_staff:
            return True
        
class IsCommentOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
    
        return request.user == obj.owner_of_comment
    