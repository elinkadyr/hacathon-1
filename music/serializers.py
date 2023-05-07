from rest_framework.serializers import ModelSerializer
from .models import Genre, Artist, Song


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
    class Meta:
        model = Song
        fields = '__all__'




