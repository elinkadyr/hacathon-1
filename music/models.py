from django.db import models
from account.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200)


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    bio = models.TextField()


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='song')
    title = models.CharField(max_length=200)
    release = models.DateField()
    duration = models.DurationField()


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)



