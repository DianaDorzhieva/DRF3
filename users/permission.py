from rest_framework.permissions import BasePermission
from users.models import User


class IsUser(BasePermission):
    message = "Вы не можете редактировать/удалять чужие привычки!"

    def has_permission(self, request, view):
        if request.user.pk == User.pk:
            return True
        return False
