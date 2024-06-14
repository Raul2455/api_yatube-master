"""
Сериализаторы для моделей Comment, Group и Post.

Преобразуют данные моделей в формат JSON и обратно.
"""
from rest_framework import serializers
from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели комментариев.

    Преобразует данные модели Comment в формат JSON и обратно.
    """

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        """
        Мета-класс для сериализатора комментариев.

        Определяет модель и поля, которые должны быть включены
        в сериализацию.
        """

        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели групп.

    Преобразует данные модели Group в формат JSON и обратно.
    """

    class Meta:
        """
        Мета-класс для сериализатора групп.

        Определяет модель и поля, которые должны быть включены
        в сериализацию.
        """

        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели постов.

    Преобразует данные модели Post в формат JSON и обратно.
    Позволяет указывать автора и группу поста.
    """

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """
        Мета-класс для сериализатора постов.

        Определяет модель и поля, которые должны быть включены
        в сериализацию.
        """

        model = Post
        fields = '__all__'
