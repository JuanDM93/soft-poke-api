from rest_framework.serializers import (
    ModelSerializer,
    UUIDField,
)

from teams.models import Team

from trainers.serializers import TrainerSerializer
from pokemons.serializers import PokemonSerializer


class TeamSerializer(ModelSerializer):

    uuid = UUIDField(read_only=True, required=False)
    owner = TrainerSerializer(read_only=True, required=False)
    members = PokemonSerializer(many=True, required=False)

    class Meta:
        model = Team
        fields = [
            'uuid',
            'name',
            'owner',
            'members',
        ]
