from django.db.models import Sum
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Comment, Favorite, Like, Rating

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
  

class RatingSerializer(ModelSerializer):
    like_ratio = SerializerMethodField()

    class Meta:
        model = Rating
        fields = ('id', 'song', 'likes', 'like_ratio')

    def get_like_ratio(self, obj):
        total_likes = obj.song.ratings.aggregate(Sum('likes'))['likes__sum']
        if total_likes:
            return obj.likes / total_likes * 100
        else:
            return 0
