from django import forms
from .models import Album
from .models import Artist
from .models import Song


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('artist', 'genre',)
        

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'genre',)
        widgets = {'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
    }


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('song',)