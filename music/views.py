from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from .models import Genre, Artist, Song, Playlist
from .serializers import GenreSerializer, ArtistSerializer, SongSerializer, PlaylistSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer 

class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 

class GenreDestroyAPIView(DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 

