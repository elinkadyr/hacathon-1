from rest_framework.serializers import ModelSerializer
from .models import Genre, Artist, Song, Playlist

class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class ArtistSerializer(ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class SongSerializer(ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class PlaylistSerializer(ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'

