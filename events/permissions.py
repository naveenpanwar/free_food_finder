from rest_framework import permissions


class IsCreatorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow if the user is an admin
        if request.user.is_superuser:
            return True
        # Allow if the user is the creator of the object
        return obj.creator == request.user
