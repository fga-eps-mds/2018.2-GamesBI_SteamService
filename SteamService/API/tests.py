from django.test import TestCase
from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from model_mommy import mommy
from SteamService.importdata.models import Game


class EndpointTestCase(APITestCase, URLPatternsTestCase):

	urlpatterns = [
		path('api/', include('SteamService.API.urls')),
	]

	def setUp(self):

		self.game_steam = mommy.make(
			Game
		)

		self.steam_endpoint = reverse('get_steam_games_Name_list')

	def tearDown(self):

		Game.object.all().delete()

	def test_status_steam_endpoint(self):

		response = self.client.get(self.steam_endpoint)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_response_steam_endpoint(self):

		response = self.client.get(self.steam_endpoint, format='json')
		self.assertEqual(Game.objects.all().count(),1)
		self.assertEqual(len(response.data),1)

		for data in response.data:
			self.assertNotEqual(data['name'], None)
			self.assertNotEqual(data['positive_reviews_steam'], None)
			self.assertNotEqual(data['negative_reviews_steam'], None)

	def test_status_name_endpoint(self):

		response = self.client.get(self.name_endpoint)
		self.assertEqual(response.status_code, status.HTTP_200_OK)




