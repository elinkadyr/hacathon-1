from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Comment, Like, Rating
from .permissions import IsAuthor
from .serializers import CommentSerializer, LikeSerializer, RatingSerializer


"""CRUD ДЛЯ КОММЕНТАРИЕВ"""
class CommentViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]


"""CRUD ДЛЯ ЛАЙКОВ"""
class LikeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return self.queryset.filter(user=self.queryset.user)

"""ИЗБРАННОЕ"""


"""CRUD ДЛЯ РЕЙТИНГА"""
class AddRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        ser = RatingSerializer(data=request.data, context={"request": request})
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=201)
