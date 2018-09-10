from SteamService.importdata.models import Game
from rest_framework.serializers import ModelSerializer

class GamesSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
