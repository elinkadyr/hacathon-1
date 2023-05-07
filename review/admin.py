from django.contrib import admin
from .models import Comment, Like, Favorite, Rating

admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Favorite)
admin.site.register(Rating)
