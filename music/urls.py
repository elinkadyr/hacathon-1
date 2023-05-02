from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, SongViewSet, GenreListCreateAPIView, GenreDestroyAPIView

router = DefaultRouter()
router.register('Artist', ArtistViewSet)
router.register('Song', SongViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('genre/', GenreListCreateAPIView.as_view()),
    path('genre/<int:pk>/', GenreDestroyAPIView.as_view()),
]