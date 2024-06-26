"""
Этот модуль настраивает приложение API в рамках проекта Django.

Он включает в себя настройки названия
приложения и автоматического типа поля по умолчанию.
"""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Этот класс представляет конфигурацию для приложения API.

    В нем указывается тип автоматического
    поля по умолчанию и название приложения.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
