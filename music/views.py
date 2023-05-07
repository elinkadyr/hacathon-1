from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from .models import Genre, Artist, Song
from .serializers import GenreSerializer, ArtistSerializer, SongSerializer


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




