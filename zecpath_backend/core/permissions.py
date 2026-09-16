
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = "Only admins can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


class IsEmployer(BasePermission):
    message = "Only employers or admins can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["EMPLOYER", "ADMIN"]
        )

class IsCandidate(BasePermission):
    message = "Only candidates or admins can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["CANDIDATE", "ADMIN"]
        )