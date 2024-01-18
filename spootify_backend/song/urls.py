from django.urls import path
from . import views

urlpatterns = [
    
    path('playlist/',views.PlayListAV.as_view(),name='playlist'),
    path('playlist/<int:pk>',views.PlayListDetailAV.as_view(),name='playlist-detail'),
    path('songs/',views.SongListAV.as_view(),name="song-list"),
    path('songs/<int:pk>/',views.SongDetailAV.as_view(),name="song-detail")

    
]
