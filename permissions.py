from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'To edite a post you should be its owner.'
    def has_object_permission(self, request, view,obj):
        return request.user == obj.user