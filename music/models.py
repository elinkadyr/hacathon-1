from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from account.models import User


"""ТАБЛИЦА ДЛЯ ЖАНРОВ"""
class Genre(models.Model):
    name = models.CharField(max_length=200)


"""ТАБЛИЦА ДЛЯ ИСПОЛНИТЕЛЕЙ"""
class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    bio = models.TextField()


"""ТАБЛИЦА ДЛЯ ПЕСЕН"""
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='song')
    title = models.CharField(max_length=200)
    release = models.DateField()
    duration = models.DurationField()


"""ТАБЛИЦА ДЛЯ ПЛЕЙЛИСТОВ"""
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


"""ТАБЛИЦА ДЛЯ КОММЕНТАРИЕВ"""
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""ТАБЛИЦА ДЛЯ ЛАЙКОВ"""
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='likes') 
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['user', 'song']


"""ТАБЛИЦА ДЛЯ ИЗБРАННОГО"""
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='favorites')

    from .models import Like
    @receiver(post_save, sender=Like)
    def add_to_favorites(sender, instance, created, **kwargs):
        if created:
            # проверяем, есть ли песня в избранном у пользователя
            favorite, created = Favorite.objects.get_or_create(user=instance.user, song=instance.song)
            if created:
                favorite.save()


"""ТАБЛИЦА ДЛЯ РЕЙТИНГА"""
class Rating(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])



