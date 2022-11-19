
from django.contrib import admin
from django.urls import path
from music_app.views import LandingPageView,ArtistCreateView,ArtistListView,ArtistUpdateView,deleteArtist
# ArtistUpdateView,deleteArtist,ArtistDeleteView,SongCreateView,SongListView,SongUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPageView.as_view(),name='home'),
    path('artists',ArtistListView.as_view(),name='artists'),
    # path('add_artist',ArtistCreateView.as_view(),name='add_artist')
    # path ('songs' ,SongsListView.as_view(),name='songs'),
    
    path('artists',ArtistListView.as_view(),name='artists'),
    path('add_artist',ArtistCreateView.as_view(),name='add_artist'),
    path('artist-details/<int:pk>', ArtistUpdateView.as_view(),name='artist_details'),
    path('artist-delete/<int:pk>', deleteArtist,name='delete_artist'),

]


