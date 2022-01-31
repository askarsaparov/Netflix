from datetime import date

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Movie, Actor, Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthdate(self, value):
        date_ = date(1950, 1, 1)
        if value < date_:
            raise ValidationError(detail="No' tog'ri kiritildi")
        else:
            return value

    def create(self, validated_data):
        instance, _ = Actor.objects.get_or_create(**validated_data)
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"