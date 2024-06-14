"""
URL-конфигурация приложения API.

Определяет маршруты для доступа к API приложения,
включая получение токенов аутентификации
и обработку запросов к постам, группам и комментариям.
"""
from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename="comment"
)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
