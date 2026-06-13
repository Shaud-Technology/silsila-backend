from rest_framework.permissions import BasePermission


class HasGroupPermission(BasePermission):

    group_name = None

    def has_permission(self, request, view):

        return request.user.groups.filter(
            name=self.group_name
        ).exists()

class IsAdmin(HasGroupPermission):
    group_name = "Admin"

class IsCreator(HasGroupPermission):
    group_name = "Creator"