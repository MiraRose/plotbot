from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)


class Character(models.Model):
    type = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
