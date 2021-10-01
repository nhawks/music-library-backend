from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
