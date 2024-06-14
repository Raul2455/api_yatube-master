"""
Модуль определяет модели для приложения posts.

Этот модуль содержит определения моделей Group, Post и Comment,
которые используются для представления групп,
постов и комментариев соответственно.
"""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """
    Модель для представления группы.

    Атрибуты:
        title (str): Название группы.
        slug (str): Уникальный идентификатор группы.
        description (str): Описание группы.
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        """Возвращает строковое представление группы."""
        return self.title


class Post(models.Model):
    """
    Модель для представления поста.

    Атрибуты:
        text (str): Текст поста.
        pub_date (datetime): Дата публикации поста.
        author (User): Автор поста.
        image (ImageField): Изображение, прикрепленное к посту.
        group (Group): Группа, к которой относится пост.
    """

    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        """Возвращает строковое представление поста."""
        return self.text[:20]  # Возвращаем первые 20 символов текста поста


class Comment(models.Model):
    """
    Модель для представления комментария.

    Атрибуты:
        author (User): Автор комментария.
        post (Post): Пост, к которому относится комментарий.
        text (str): Текст комментария.
        created (datetime): Дата создания комментария.
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    def __str__(self):
        """Возвращает строковое представление комментария."""
        return self.text[:20]
