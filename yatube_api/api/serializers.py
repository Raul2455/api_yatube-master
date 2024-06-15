"""Сериализаторы для моделей Comment, Group и Post."""

from rest_framework import serializers

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """
        Подкласс для хранения данных и.

        настроек сериализатора комментариев.
        """

        model = Comment
        fields = '__all__'
        read_only_fields = ['post']


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели групп."""

    class Meta:
        """
        Подкласс для хранения данных и.

        настроек сериализатора групп.
        """

        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели постов."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """
        Подкласс для хранения данных и.

        настроек сериализатора постов.
        """

        model = Post
        fields = '__all__'
