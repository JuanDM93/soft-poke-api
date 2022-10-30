from django.urls import path

from pokemons.views import (
    PokemonList,
    PokemonDetail,
)


urlpatterns = [
    path('', PokemonList.as_view(), name='pokemon-list'),
    path('<uuid:pk>', PokemonDetail.as_view(), name='pokemon-detail'),
]
