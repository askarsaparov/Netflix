# Generated by Django 4.0.1 on 2022-01-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_movie_actors'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb',
            field=models.SmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
    ]
