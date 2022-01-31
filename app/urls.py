from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from app.views import MovieViewSet, ActorViewSet, MovieActorAPIView, CommentAPIView, CommentDetailAPIView

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view()),

    path('comments/', CommentAPIView.as_view()),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view()),
    path('auth/', obtain_auth_token),
]