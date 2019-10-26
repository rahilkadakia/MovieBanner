from django.db import models

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    runtime = models.TimeField(max_length=20)
    rating = models.CharField(max_length=2)
    genre = models.CharField(max_length=100)
    release_date = models.DateField(max_length=10)

    def __str__(self):
        return self.movie_name