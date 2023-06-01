"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from music import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.random_deck, name='home'),
    path('music/random_song', views.random_song, name='random-song'),
    path('music/deck_list', views.deck_list, name='deck-list'),
    path('artist/artist_list', views.artist_list, name='artist-list'),
    path('album/album_list', views.album_list, name='album-list'),
    # path('artist/<int:pk>/', views.artist_detail, name='artist-detail'),
    path('music/new', views.create_album, name='new-album'),
    path('music/<int:pk>/delete', views.delete_album, name='delete-album'),
    path('music/<int:pk>/edit', views.edit_album, name='edit-album')
]