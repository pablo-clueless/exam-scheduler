from rest_framework import permissions

class IsStudent(permissions.BasePermission):
    """
    Custom permission to only allow students to access specific views.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'student'

class IsSupervisor(permissions.BasePermission):
    """
    Custom permission to only allow supervisors to access specific views.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'supervisor'

class IsExamOfficer(permissions.BasePermission):
    """
    Custom permission to only allow exam officers to access specific views.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'exam_officer'
