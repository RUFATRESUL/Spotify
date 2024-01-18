from django.urls import path
from . import views

urlpatterns = [
    path('liked-playlists/',views.LikedPlayListAV.as_view(), name='liked-playlists'),
    path('like-playlist/<int:pk>/',views.liked_playlist,name='like-playlist'),
    path('unlike-playlist/<int:pk>/',views.unlike_playlist,name='unlike-playlist'),
    path('liked-songs/',views.LikedSongListAV.as_view(),name='liked-songs'),
    path('like-songs/<int:pk>/',views.liked_songs,name='like-songs'),
    path('unlike-songs/<int:pk>/',views.unlike_songs,name='unlike-songs'),
    path('following-artists/',views.FollowingListAV.as_view(),name="following-lists"),
    path('follow-artist/<int:pk>/',views.follow_artist,name='follow-artist'),
    path('unfollow-artist/<int:pk>/',views.unfollow_artist,name='unfollow-artist'),
    path('artists/',views.ArtistsListAV.as_view(),name='artists'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    
]
