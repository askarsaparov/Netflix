from django.test import TestCase, Client

from app.models import Movie


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Test Movie', year='2022-01-27', genre='Test Genre', imdb=1)
        self.movie2 = Movie.objects.create(name='Test Movie2', year='2022-02-27', genre='Test Genre2', imdb=2)
        self.movie3 = Movie.objects.create(name='Test Movie3', year='2022-03-27', genre='Test Genre3', imdb=3)
        self.movie4 = Movie.objects.create(name='Test Movie4', year='2022-04-27', genre='Test Genre4', imdb=4)
        self.movie5 = Movie.objects.create(name='Test Movie5', year='2022-05-27', genre='Test Genre5', imdb=5)
        self.client = Client()

    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 5)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], "Test Movie")
        self.assertEquals(data[0]['year'], "2022-01-27")
        self.assertEquals(data[0]['genre'], "Test Genre")
        self.assertEquals(data[0]['imdb'], 1)
        self.assertEquals(len(data[0]['actors']), 0)

    def test_search_movie(self):
        response = self.client.get('/movies/?search=Test')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 5)
        self.assertEquals(data[0]['name'], "Test Movie")

    def test_ordering_movie(self):
        response1 = self.client.get('/movies/?ordering=imdb')
        response2 = self.client.get('/movies/?ordering=-imdb')
        data1 = response1.data
        data2 = response2.data

        self.assertEquals(response1.status_code, 200)
        self.assertEquals(response2.status_code, 200)

        self.assertEquals(len(data1), 5)
        self.assertEquals(len(data2), 5)

        self.assertEquals(data1[0]['imdb'], 1)
        self.assertEquals(data1[1]['imdb'], 2)
        self.assertEquals(data1[2]['imdb'], 3)
        self.assertEquals(data1[3]['imdb'], 4)
        self.assertEquals(data1[4]['imdb'], 5)

        self.assertEquals(data2[0]['imdb'], 5)
        self.assertEquals(data2[1]['imdb'], 4)
        self.assertEquals(data2[2]['imdb'], 3)
        self.assertEquals(data2[3]['imdb'], 2)
        self.assertEquals(data2[4]['imdb'], 1)