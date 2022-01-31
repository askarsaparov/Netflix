from django.db import models

from app.models.actor import Actor


class Movie(models.Model):
    choice_imdb = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    name = models.CharField(max_length=200, blank=False, null=False)
    year = models.DateField(blank=False, null=False)
    imdb = models.SmallIntegerField(choices=choice_imdb,blank=True, null=True)
    genre = models.CharField(max_length=300, blank=False, null=False)
    actors = models.ManyToManyField(Actor, blank=True, null=True)

    def __str__(self):
        return self.name