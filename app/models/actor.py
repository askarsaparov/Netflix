from django.db import models

class Actor(models.Model):
    genre_choice = (
        ('erkak', 'erkak'),
        ('ayol', 'ayol'),
    )
    name = models.CharField(max_length=200, blank=False, null=False)
    birthdate = models.DateField()
    gender = models.CharField(max_length=100, choices=genre_choice)

    def __str__(self):
        return self.name