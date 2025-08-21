from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, obj):
        # SAFE_METHODS are GET, HEAD and OPTION meaning that anyone can view
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Otherwise only the author or owner can modify
        return obj.author == request.user