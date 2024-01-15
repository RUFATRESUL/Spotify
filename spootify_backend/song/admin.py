from django.contrib import admin
from .models import Song,Playlist,Genre

# Register your models here.
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Genre)
