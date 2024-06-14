"""
API ViewSets для приложения Posts.

включая представления для постов, групп и комментариев.
"""
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import GroupSerializer, PostSerializer, CommentSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Набор вьюсетов для просмотра экземпляров групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Набор вьюсетов для просмотра и редактирования экземпляров записей."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """
        Сохраняет экземпляр записи с указанием автора.

        присвоенного текущему пользователю.
        """
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Набор вьюсетов для просмотра и.

    редактирования экземпляров комментариев.
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        """Возвращает комментарии к указанному сообщению."""
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        """
        Сохраняет экземпляр комментария.

        указав в качестве автора текущего пользователя,
        а в качестве записи - указанную запись.
        """
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        """
        Обновляет экземпляр комментария.

        указав в качестве автора текущего пользователя,
        а в качестве записи - исходную запись.
        """
        serializer.save(author=self.request.user, post=self.get_object().post)
