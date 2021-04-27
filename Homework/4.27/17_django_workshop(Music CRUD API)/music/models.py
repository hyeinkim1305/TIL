from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=10)

class Music(models.Model):
    title = models.CharField(max_length=10)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    