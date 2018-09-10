from rest_framework.viewsets import ModelViewSet
from SteamService.importdata.models import Game
from .serializers import GamesSerializer

class GamesViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GamesSerializer
