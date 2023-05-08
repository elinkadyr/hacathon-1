from rest_framework.serializers import ModelSerializer
from .models import Genre, Artist, Song, Playlist
from .helpers import send_spam

from review.serializers import RatingSerializer
"""СЕРИАЛИЗАТОР ДЛЯ ЖАНРОВ"""
class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


"""СЕРИАЛИЗАТОР ДЛЯ ИСПОЛНИТЕЛЕЙ"""
class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


"""СЕРИАЛИЗАТОР ДЛЯ ПЕСЕН"""
class SongSerializer(ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'ratings')

    def create(self, validated_data):
        send_song = super().create(validated_data)
        send_spam(send_song)
        return send_song

"""СЕРИАЛИЗАТОР ДЛЯ ПЛЕЙЛИСТОВ"""
class PLaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

