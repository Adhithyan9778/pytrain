
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = "Only admins can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


class IsEmployer(BasePermission):
    message = "Only employers can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "EMPLOYER"
        )


class IsCandidate(BasePermission):
    message = "Only candidates can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "CANDIDATE"
        )