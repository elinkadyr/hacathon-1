from django.db import models
from account.models import User
from music.models import Song


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
    is_fav = models.BooleanField(default=False)


"""ТАБЛИЦА ДЛЯ ИЗБРАННОГО"""
class Favorite(models.Model):
    ...


"""ТАБЛИЦА ДЛЯ РЕЙТИНГА"""
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    songs = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(choices=[(1, 1),(2, 2),(3, 3),(4, 4),(5, 5)])