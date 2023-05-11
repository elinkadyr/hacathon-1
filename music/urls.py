from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AddFavoriteView, ArtistViewSet, CommentViewSet,
                    GenreDestroyAPIView, GenreListCreateAPIView, LikeViewSet,
                    SongViewSet)


router = DefaultRouter()
router.register('artist', ArtistViewSet)
router.register('song', SongViewSet)
router.register("comments", CommentViewSet)
router.register("likes", LikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('genre/', GenreListCreateAPIView.as_view()),
    path('genre/<int:pk>/', GenreDestroyAPIView.as_view()),
    path("user-favorite/", AddFavoriteView.as_view()),
]
