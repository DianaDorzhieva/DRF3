from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    message = "Вы не можете редактировать/удалять чужие привычки!"

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
