from django.contrib import admin
from .models import Genre, Artist, Song


admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
