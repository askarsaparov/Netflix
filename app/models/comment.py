from django.contrib.auth import get_user_model
from django.db import models

from app.models import Movie

User = get_user_model()


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    created_date = models.DateField(auto_now=True)