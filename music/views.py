from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import DestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet


from .models import Artist, Genre, Song
from .serializers import ArtistSerializer, GenreSerializer, SongSerializer


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

    # def post(self, request, song_id):
    #     song = get_object_or_404(Song, id=song_id)
    #     user = request.user
    #     user.liked_songs.add(song)
    #     song.increase_likes()
    #     return Response({'status': 'liked'})
    




