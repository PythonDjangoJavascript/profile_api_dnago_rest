from rest_framework import permissions


class IsOwnProfileOrReadOnly(permissions.BasePermission):
    """Provide permission to update users own profile and allow to 
    view others profile"""

    def has_object_permission(self, request, view, obj):
        """Over riiding baspermission's permisson method"""

        if request.method in permissions.SAFE_METHODS:
            return True
        # here obj is our profile object and it has user child
        return obj.user == request.user


class IsOwnStatusOrReadOnly(permissions.BasePermission):
    """Provie Permission to edit own status and retrieve all profile statuses"""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile == request.user.profile
