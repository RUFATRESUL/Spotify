from rest_framework import serializers
from user.serializers import CustomerInfoSerializer
from .models import (
    Playlist,
    Song,
    Genre
)

class PlayListSerializer(serializers.ModelSerializer):

    author = CustomerInfoSerializer()

    class Meta:
        model = Playlist
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        exclude = ['lyrics']

class SongDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'