from django.db import models

# Create your models here.

GENDER_CHOICE = [
    ['male','Male'],
    ['female','Female']
]

class Customer(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    image = models.ImageField()
    liked_songs = models.ManyToManyField('song.Song',related_name='liked_songs',null=True,blank=True)
    liked_playlist = models.ManyToManyField('song.PlayList',related_name='liked_playlists',null=True,blank=True)
    followed_artists = models.ManyToManyField('Artist',related_name='followed_artists',null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField( max_length=20,choices=GENDER_CHOICE)
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    

class Artist(models.Model):

    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    image = models.ImageField('artist/images/')
    cover = models.ImageField('artist/covers',null=True,blank=True)
    verfied = models.BooleanField(default=False)
    updated = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    