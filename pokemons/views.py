from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from pokemons.models import Pokemon
from pokemons.serializers import PokemonDetailSerializer
from teams.models import Team


class TeamLimitExceeded(ValidationError):
    default_detail = 'A team can have no more than 6 pokemons'
    status_code = 400


class PokemonList(ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_team(self):
        return Team.objects.get(uuid=self.kwargs['uuid'])

    def get_queryset(self):
        team = self.get_team()
        return team.members.all()

    def perform_create(self, serializer):
        team = self.get_team()
        if team.members.count() >= 6:
            raise TeamLimitExceeded
        team.members.add(serializer.save())
        team.save()


class PokemonDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_team(self):
        return Team.objects.get(uuid=self.kwargs['uuid'])

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return Pokemon.objects.none()
        team = self.get_team()
        return team.members.all()

    def perform_update(self, serializer):
        team = self.get_team()
        if team.members.count() >= 6:
            raise TeamLimitExceeded
        team.members.add(serializer.save())
        team.save()

    def perform_destroy(self, instance):
        team = self.get_team()
        team.members.remove(instance)
        team.save()
