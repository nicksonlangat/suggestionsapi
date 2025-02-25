from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access the view.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
        
class AllowAnyForCreateOnly(permissions.BasePermission):
    """
    Custom permission to allow anyone to create, but only admins to retrieve, update or delete.
    """
    def has_permission(self, request, view):
        # Allow anyone to create a feedback entry
        if request.method == 'POST':
            return True
        # Only allow admin users to list, retrieve, update or delete
        return request.user and request.user.is_staff