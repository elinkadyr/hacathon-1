from rest_framework.serializers import ModelSerializer

from .helpers import send_spam
from .models import Genre, Artist, Song, Playlist, Comment, Like, Favorite, Rating


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


"""СЕРИАЛИЗАТОР ДЛЯ КОММЕНТАРИЕВ"""
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs


"""СЕРИАЛИЗАТОР ДЛЯ ЛАЙКОВ"""
class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs

    def to_representation(self, instance: Like):
        from music.serializers import SongSerializer

        rep = super().to_representation(instance)
        rep["song"] = SongSerializer(instance.song).data
        return rep


"""СЕРИАЛИЗАТОР ДЛЯ ИЗБРАННОГО"""
class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs

    def to_representation(self, instance: Favorite):
        from music.serializers import SongSerializer

        rep = super().to_representation(instance)
        rep["favorite"] = SongSerializer(instance.song).data
        return rep


"""СЕРИАЛИЗАТОР ДЛЯ РЕЙТИНГА"""
class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'song', 'likes')


