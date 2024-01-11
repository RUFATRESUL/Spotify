from django.db import models

# Create your models here.



class Customer(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    image = models.ImageField()
    liked_songs = models.ManyToManyField('song.Song',related_name='liked_songs')
    liked_playlist = models.ManyToManyField('song.PlayList',related_name='liked_playlists')
    followed_artists = models.ManyToManyField('Artist',related_name='followed_artists')
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)

class Artist(models.Model):

    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    image = models.ImageField('artist/images/')
    cover = models.ImageField('artist/covers')
    verfied = models.BooleanField(default=False)
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)
    