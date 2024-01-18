from django.db import models

# Create your models here.


class Genre(models.Model):
    title = models.CharField()
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Playlist(models.Model):
    title = models.TextField()
    author = models.ForeignKey('user.Customer',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='playlist/images/')
    featured = models.BooleanField(default=False)
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Song(models.Model):
    title = models.TextField()
    image = models.ImageField('songs/images/')
    audio = models.FileField('songs/audios/')
    artist = models.ManyToManyField('user.Artist',related_name='songs')
    duration = models.IntegerField()
    lyrics = models.TextField(null=True,blank=True)
    genres = models.ManyToManyField(Genre,related_name='songs')
    playlists = models.ManyToManyField(Playlist,null=True,blank=True,related_name='songs')
    listen_count = models.BigIntegerField(default=0)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

