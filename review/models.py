from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

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
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['user', 'song']


"""ТАБЛИЦА ДЛЯ ИЗБРАННОГО"""
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
from review.models import Like


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
    likes = models.PositiveIntegerField(default=0)
