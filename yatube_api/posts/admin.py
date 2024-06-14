"""
Модуль администрирования для приложения posts.

Здесь настроены классы административной панели
для моделей Post, Group и Comment,
что позволяет управлять этими сущностями
через административный интерфейс Django.
"""

from django.contrib import admin

from .models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    """
    Класс администрирования для модели Post.

    Определяет отображение списка постов, фильтрацию, поиск и другие параметры
    интерфейса административной панели для модели Post.
    """

    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
