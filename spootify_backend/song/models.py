from django.db import models

# Create your models here.


class Genre(models.Model):
    title = models.CharField()
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)


class Playlist(models.Model):
    title = models.TextField()
    author = models.ForeignKey('user.Customer',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='playlist/images/')
    featured = models.BooleanField(default=False)
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)





class Song(models.Model):
    title = models.TextField()
    image = models.ImageField('songs/images/')
    audio = models.FileField('songs/audios/')
    artist = models.ManyToManyField('user.Artist')
    duration = models.IntegerField()
    lyrics = models.TextField(null=True,blank=True)
    genres = models.ManyToManyField(Genre)
    playlists = models.ManyToManyField(Playlist)
    listen_count = models.BigIntegerField(default=0)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

