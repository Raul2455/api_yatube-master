"""API ViewSets для приложения Posts."""

from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from posts.models import Group, Post
from api.permissions import IsAuthorOrReadOnly
from api.serializers import GroupSerializer, PostSerializer, CommentSerializer


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
        post = self.get_post()
        return post.comments

    def perform_create(self, serializer):
        """
        Сохраняет экземпляр комментария.

        указав в качестве автора текущего пользователя,
        а в качестве записи - указанную запись.
        """
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)

    def get_post(self):
        """Возвращает указанный пост."""
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))
