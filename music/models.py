from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Artist(models.Model):
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'artists'

    def __str__(self):
        return self.artist


class Album(models.Model):
    artist = models.ForeignKey(
        to='Artist', on_delete=models.CASCADE, blank=True, null=True, default=None)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='media/images/')

    class Meta:
        verbose_name_plural = 'albums'

    def __str__(self):
        return self.title


class Song(models.Model):
    song = models.CharField(max_length=200, blank=True, null=True)
    artist = models.ForeignKey(
        to='Artist', on_delete=models.CASCADE, blank=True, null=True, default=None)
    album = models.ForeignKey(
        to='Album', on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.song


class Deck(models.Model):
    word = models.CharField(max_length=50)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.word