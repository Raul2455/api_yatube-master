"""
Модуль определяет пользовательские разрешения.

для работы с объектами в API.
"""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение.

    которое позволяет редактировать объект только его владельцам.
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверяет, имеет ли пользователь разрешение на работу с объектом.

        Разрешает доступ на чтение всем пользователям,
        но на редактирование - только авторам объекта.
        """
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
