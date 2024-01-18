from django.urls import path
from . import views

urlpatterns = [
    path('liked-playlists/',views.LikedPlayListAV.as_view(), name='liked-playlists'),
    path('like-playlist/<int:pk>/',views.liked_playlist,name='like-playlist'),
    path('unlike-playlist/<int:pk>/',views.unlike_playlist,name='unlike-playlist'),
    path('like-songs/<int:pk>/',views.liked_songs,name='like-songs'),
    path('unlike-songs/<int:pk>/',views.unlike_songs,name='unlike-songs'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    
]
