from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.models import Movie, Actor, Comment
from app.serializers import MovieSerializer, ActorSerializer, CommentSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['imdb', '-imdb']
    filter_fields = ['genre']

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        movie.actors.add(serializer.data['id'])
        return Response(data=serializer.data)

    @action(detail=True, methods=['DELETE'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor = Actor.objects.get(name=request.data['name'], birthdate=request.data['birthdate'],
                                  gender=request.data['gender'])
        if actor not in movie.actors.all():
            return Response(data={"massage": f"Not is {actor} in film"})
        else:
            movie.actors.remove(actor)
            return Response(data={"massage": f"REMOVE: {actor}"})


class MovieActorAPIView(APIView):
    def get(self, request, *args, **kwargs):
        movie = Movie.objects.get(pk=kwargs['id'])
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(data=serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        serializers = CommentSerializer(comments, many=True)
        return Response(data=serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class CommentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
