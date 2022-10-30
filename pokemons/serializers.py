import requests
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    CharField,
    ValidationError,
)

from pokeapi.settings import POKEMON_API_URL

from pokemons.models import Pokemon


class PokemonSerializer(ModelSerializer):
    """Basic Pokemon serializer."""
    class Meta:
        model = Pokemon
        fields = [
            'uuid',
            'name',
        ]


class PokemonDetailSerializer(ModelSerializer):
    """Pokemon serializer with details from external API."""

    name = CharField()
    info = SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = [
            'uuid',
            'name',
            'info',
        ]

    def get_pokemon(self, name):
        """
        Get pokemon info from external API
        """
        response = requests.get(POKEMON_API_URL + name)
        if response.status_code == 404:
            raise ValidationError('Pokemon not found')
        if response.status_code != 200:
            raise ValidationError('Pokemon API is down')
        return response.json()

    def get_info(self, obj):
        pokemon = self.get_pokemon(obj.name)
        return pokemon

    def validate(self, attrs):
        self.get_pokemon(attrs['name'].lower())
        attrs['owner'] = self.context['request'].user.trainer
        return attrs
