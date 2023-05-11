from django.contrib import admin

from .models import Genre, Artist, Song, Comment, Like, Favorite, Rating


admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Favorite)
admin.site.register(Rating)
