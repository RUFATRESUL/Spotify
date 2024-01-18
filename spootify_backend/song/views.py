from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Playlist,Song
from .serializers import (
    PlayListSerializer,
    SongSerializer,
    SongDetailSerializer
)

# Create your views here.

class PlayListAV(ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlayListSerializer

class PlayListDetailAV(ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlayListSerializer

class SongListAV(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer
   