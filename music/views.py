from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, Song, Artist, Album 
from .forms import AlbumForm
import random


def random_deck(request):
    decks = Deck.objects.all()
    deck = random.choice(decks)
    songs = Song.objects.all()
    song = random.choice(songs)
    return render(request, 'music/index.html', {'deck': deck, 'song': song})


def random_song(request):
    songs = Song.objects.all()
    song = random.choice(songs)
    return render(request, 'music/index.html', {'song': song})


# THIS IS WHERE THE ERROR IS SHOWING AN ISSUE
def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'music/index.html', {'decks': decks})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(request.POST, instance=album)
        form.save()
        return redirect('album-detail', pk=pk)
    return render(request, 'music/edit_album.html',  {'form': form})


def create_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        form.save()
        return redirect('album_list')
    return render(request, 'music/new_album.html', {'form': form})