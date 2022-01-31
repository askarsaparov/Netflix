from django.contrib import admin

from app.models import Movie, Actor, Comment

admin.site.register([Movie, Actor, Comment])
