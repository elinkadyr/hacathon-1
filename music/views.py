from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Artist, Comment, Favorite, Genre, Like, Song
from .permissions import IsAuthor
from .serializers import (ArtistSerializer, CommentSerializer,
                          FavoriteSerializer, GenreSerializer, LikeSerializer,
                          SongSerializer)

"""CREATE ДЛЯ ЖАНРОВ"""
class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 


"""DELETE ДЛЯ ЖАНРОВ"""
class GenreDestroyAPIView(DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 


"""CRUD ДЛЯ АРТИСТОВ"""
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


"""CRUD ДЛЯ ПЕСЕН"""
class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer 
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['genre',]
    search_fields = ['title',]


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

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



"""ИЗБРАННОЕ"""
class AddFavoriteView(CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        like_serializer = self.serializer_class(data=request.data)
        like_serializer.is_valid(raise_exception=True)
        user = self.request.user
        song_id = like_serializer.validated_data.get('song')
        song = get_object_or_404(Song, pk=song_id)
        like, created = Like.objects.get_or_create(user=user, song=song)
        if created:
            Favorite.objects.create(user=user, song=song)
        return Response(like_serializer.data, status=201)


"""РЕЙТИНГ ОСНОВАННЫЙ НА ЛАЙКАХ"""
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def add_rating(request, d_id):
#     """
#     User can add a rating to doctor
#     """
#     user = request.user
#     doctor = get_object_or_404(Song, id=d_id)
#     value = request.POST.get("value")

#     if not value:
#         raise ValueError("Value is required")

#     if Rating.objects.filter(user=user, song=song, value=value).exists():
#         rating = Rating.objects.get(user=user, doctor=doctor)
#         rating.value = value
#         rating.save()
#     else:
#         Rating.objects.create(user=user, doctor=doctor, value=value)

#     return Response("Rating created", 201)






    # def post(self, request, song_id):
    #     song = get_object_or_404(Song, id=song_id)
    #     user = request.user
    #     user.liked_songs.add(song)
    #     song.increase_likes()
    #     return Response({'status': 'liked'})
    


# class SongRatingAPIView(APIView):
#     def patch(self, request, pk):
#         song_rating = Rating.objects.filter(product_id=pk).first()
#         if song_rating is None:
#             song_rating = Rating.objects.create(product_id=pk)
#         song_rating.likes += 1
#         song_rating.save()
#         return Response({"message": "Product rating updated successfully."}, status=200)

    

# class LikeBasedRatingAPIView(APIView):
#     def get(self, request):
#         # Получаем общее количество лайков для каждого объекта рейтинга
#         ratings = Rating.objects.annotate(total_likes=Sum('like'))
#         # Получаем общее количество лайков для всех объектов рейтинга
#         total_likes = ratings.aggregate(Sum('like'))['like__sum']
#         # Считаем процентное соотношение лайков для каждого объекта рейтинга
#         for rating in ratings:
#             rating.like_ratio = rating.likes / total_likes * 100 if total_likes else 0
#         # Сортируем объекты рейтинга по убыванию процентного соотношения лайков
#         sorted_ratings = sorted(ratings, key=lambda r: r.like_ratio, reverse=True)
#         # Возвращаем результат в виде списка отсортированных объектов рейтинга
#         serializer = RatingSerializer(sorted_ratings, many=True)
#         return Response(serializer.data)



# class LikeBasedRatingAPIView(APIView):
#     def get(self, request):
#         # Получаем общее количество лайков для каждой песни
#         songs_likes = Rating.objects.values('song').annotate(total_likes=Sum('likes'))
#         # Получаем общее количество лайков для всех песен
#         total_likes = Rating.objects.aggregate(Sum('likes'))['likes__sum']
#         # Считаем процентное соотношение лайков для каждой песни
#         for song_likes in songs_likes:
#             song_likes['like_ratio'] = song_likes['total_likes'] / total_likes * 100 if total_likes else 0
#         # Сортируем песни по убыванию процентного соотношения лайков
#         sorted_songs = sorted(songs_likes, key=lambda s: s['like_ratio'], reverse=True)
#         # Получаем отсортированный список объектов модели Rating, используя subquery
#         subquery = Rating.objects.filter(song_id=OuterRef('song')).values('song_id').annotate(like_ratio=F('likes') / total_likes * 100).values('like_ratio')
#         sorted_ratings = Rating.objects.filter(song_id__in=[s['song'] for s in sorted_songs]).annotate(like_ratio=Subquery(subquery, output_field=FloatField())).order_by('-like_ratio')
#         # Возвращаем результат в виде списка отсортированных объектов рейтинга
#         serializer = RatingSerializer(sorted_ratings, many=True)
#         return Response(serializer.data)
