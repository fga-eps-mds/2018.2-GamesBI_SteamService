from django.urls import include, path
from .views import GamesListView


urlpatterns = [
    path('get_steam_games_list/',
         GamesListView.as_view(),
         name="get_steam_games_list"),
    # retorna uma lista com os dados  de todos os games salvos no banco de dados
]
