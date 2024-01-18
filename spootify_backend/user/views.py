from django.shortcuts import render,get_object_or_404

from rest_framework.decorators import api_view,throttle_classes,permission_classes
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import(
    RegisterSerializer,
    CustomerInfoSerializer
)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from song.serializers import(
    PlayListSerializer,
    SongSerializer
)
from song.models import (
    Playlist,
    Song
)

class LikedPlayListAV(ListAPIView):
    def get_queryset(self):
        return self.request.user.customer.liked_playlist.all()
    
    serializer_class=PlayListSerializer
    permission_classes = [IsAuthenticated]

class LikedSongListAV(ListAPIView):
    def get_queryset(self):
        return self.request.user.customer.liked_songs.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def liked_playlist(request,pk):
    playlist = get_object_or_404(Playlist,pk=pk)
    request.user.customer.liked_playlist.add(playlist)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_playlist(request,pk):
    playlist = get_object_or_404(Playlist,pk=pk)
    request.user.customer.liked_playlist.add(playlist)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def liked_songs(request,pk):
    song = get_object_or_404(Song,pk=pk)
    request.user.customer.liked_songs.add(song)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_songs(request,pk):
    song = get_object_or_404(Song,pk=pk)
    request.user.customer.liked_songs.add(song)
    return Response(status=status.HTTP_202_ACCEPTED)



@api_view(['POST'])
@throttle_classes([AnonRateThrottle,UserRateThrottle])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
@throttle_classes([AnonRateThrottle,UserRateThrottle])
def login_view(request):
    user_info = request.data.get('user_info')
    password = request.data.get('password')
    
    if '@' in user_info:
        user = User.objects.filter(email=user_info).first()
    else:
        user = User.objects.filter(username=user_info).first()

    if user and user.check_password(password):
        serializer = CustomerInfoSerializer(instance=user.customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(data={'message':'User info or password is incorrect !'}, status=status.HTTP_400_BAD_REQUEST)

