import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game
from .serializers import GameSerializer


class SteamView(APIView):
    '''
        View that calls SteamSpy API
        and return some relevant
        information about a game
        and filter for Null value
    '''
    def get(self, request, format=None):


        url = 'http://igdbweb:8000/get_igdb_games_list/Id_Steam'
        header = {'Accept': 'application/json'}
        id_data = requests.get(url, headers=header)
        ndata = id_data.json()

        for game_id in ndata:
            game_data = self.get_game_data(game_id['steam'])
            filter_game_data = self.filter_game_data(game_data)
            if filter_game_data:
                self.save_game(filter_game_data)

        games = Game.objects.all()
        games_data = []
        for game in games:
            game_data = {
                'id': game.id,
                'name': game.name,
                'positive_reviews_steam': game.positive,
                'negative_reviews_steam': game.negative,
                'owners': game.owners,
                'average_forever': game.average_forever,
                'average_2weeks': game.average_2weeks,
                'price': game.price,
                'lenguages': game.languages
            }
            games_data.append(game_data)

        return Response(data=games_data)

    def get_game_data(self, game_id):
        url = 'http://steamspy.com/api.php?request=appdetails&appid={}'.format(game_id)
        header = {'Accept': 'application/json'}
        gamedata = requests.get(url, headers=header)
        ndata = gamedata.json()
        return ndata

    def filter_game_data(self, gamedata):

        if 'appid' in gamedata:
            id = gamedata['appid']
        else:
            id = None

        if 'name' in gamedata:
            name = gamedata['name']
        else:
            name = None

        if 'positive' in gamedata:
            positive = gamedata['positive']
        else:
            positive = None

        if 'negative' in gamedata:
            negative = gamedata['negative']
        else:
            negative = None

        if 'owners' in gamedata:
            owners_str = gamedata['owners']
            owners = self.read_owners(owners_str)
        else:
            owners_str = None

        if 'average_forever' in gamedata:
            average_forever = gamedata['average_forever']
        else:
            average_forever = None

        if 'average_2weeks' in gamedata:
            average_2weeks = gamedata['average_2weeks']
        else:
            average_2weeks = None

        if 'price' in gamedata:
            price = gamedata['price']
        else:
            price = None

        if 'languages' in gamedata:
            languages = gamedata['languages']
        else:
            languages = None

        filtered_data = {
            'id': id,
            'name': name,
            'positive_reviews_steam': positive,
            'negative_reviews_steam': negative,
            'owners': owners,
            'average_forever': average_forever,
            'average_2weeks': average_2weeks,
            'price': price,
            'lenguages': languages
        }
        return filtered_data

    def save_game(self, filtered_data):
        new_game = Game(
            id=filtered_data['id'],
            name=filtered_data['name'],
            positive_reviews_steam=filtered_data['positive_reviews_steam'],
            negative_reviews_steam=filtered_data['negative_reviews_steam'],
            owners=filtered_data['owners'],
            average_forever=filtered_data['average_forever'],
            average_2weeks=filtered_data['average_2weeks'],
            price=filtered_data['price'],
            lenguages=filtered_data['lenguages'],
        )
        new_game.save()

    def read_owners(self, str_owners):
        vector_numbers = self.valid_owners(str_owners)
        average = self.calculates_avarege(vector_numbers)
        return average

    def valid_owners(self, str_owners):
        low_average = str_owners.split(" .. ")[0]
        high_average = str_owners.split(" .. ")[1]
        low_average_valid = ""
        for number in low_average:
            if number != ",":
                low_average_valid = low_average_valid + number

        high_average_valid = ""
        for number in high_average:
            if number != ",":
                high_average_valid = high_average_valid + number

        low_average_int = int(low_average_valid)
        high_average_int = int(high_average_valid)
        return [low_average_int, high_average_int]

    # This method takes a vector of numbers and
    # calculates the mean between them
    def calculates_avarege(self, numbers):
        sum = 0
        for number in numbers:
            sum = sum + number
        return sum / len(numbers)
