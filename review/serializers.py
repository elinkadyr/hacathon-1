from rest_framework.serializers import ModelSerializer
from .models import Comment, Like, Favorite, Rating

"""СЕРИАЛИЗАТОР ДЛЯ КОММЕНТАРИЕВ"""
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs

    # def to_representation(self, instance: Comment):
    #     rep = super().to_representation(instance)
    #     rep["user"] = {"id": instance.user.id, "email": instance.user.email}
    #     return rep


"""СЕРИАЛИЗАТОР ДЛЯ ЛАЙКОВ"""
class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs

    # def to_representation(self, instance: Like):
    #     from music.serializers import ProductSerializer

    #     rep = super().to_representation(instance)
    #     rep["product"] = ProductSerializer(instance.product).data
    #     return rep


"""СЕРИАЛИЗАТОР ДЛЯ ИЗБРАННОГО"""
class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs
  
  
"""СЕРИАЛИЗАТОР ДЛЯ РЕЙТИНГА"""
class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs["user"] = self.context["request"].user
        return attrs

    def create(self, validated_data):
        value = validated_data.pop("value")
        obj, created = Rating.objects.update_or_create(**validated_data, defaults={"value": value})
        return obj


