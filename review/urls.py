from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, LikeViewSet, AddFavoriteView, LikeBasedRatingAPIView


router = DefaultRouter()
router.register("comments", CommentViewSet)
router.register("likes", LikeViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("user-favorite/", AddFavoriteView.as_view()),
    path("rating/", LikeBasedRatingAPIView.as_view()),
]
