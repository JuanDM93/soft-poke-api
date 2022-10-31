from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from trainers.models import Trainer
from teams.models import Team
from pokemons.models import Pokemon


class PokemonTests(APITestCase):
    def setUp(self):
        self.admin = get_user_model().objects.create_superuser(
            email='admin@mail.test',
            username='admin',
            password='admin',
        )
        self.trainer = Trainer.objects.create(
            user=get_user_model().objects.create_user(
                username='trainer',
                password='trainer',
            )
        )
        self.team = Team.objects.create(
            name='Team 1',
            trainer=self.trainer,
        )
        self.pokemon = Pokemon.objects.create(
            name='pikachu',
            trainer=self.trainer,
        )
        self.team.members.add(self.pokemon)
        self.base_url = "/api/teams/"

    def test_pokemon_list(self):
        """
        Ensure we can list pokemons.
        """
        endpoint = self.base_url + f'{self.team.pk}/pokemons/'
        self.client.force_authenticate(user=self.trainer.user)
        response = self.client.get(endpoint, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pokemon.objects.count(), 1)

    def test_pokemon_detail(self):
        """
        Ensure we can retrieve a pokemon.
        """
        self.client.force_authenticate(user=self.trainer.user)
        endpoint = self.base_url + f'{self.team.pk}/pokemons/'
        response = self.client.get(
            endpoint, format='json',
            kwargs={'pk': self.pokemon.pk}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'pikachu')

    def test_pokemon_create(self):
        """
        Ensure we can create a pokemon.
        """
        self.client.force_authenticate(user=self.trainer.user)
        endpoint = self.base_url + f'{self.team.pk}/pokemons/'
        data = {
            'name': 'bulbasaur',
            'trainer': self.trainer.pk,
        }
        response = self.client.post(endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pokemon.objects.count(), 2)

    def test_pokemon_delete(self):
        """
        Ensure we can delete a pokemon.
        """
        self.client.force_authenticate(user=self.trainer.user)
        endpoint = self.base_url + \
            f'{self.team.pk}/pokemons/' + f'{self.pokemon.pk}'
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pokemon_update(self):
        """
        Ensure we can update a pokemon.
        """
        self.client.force_authenticate(user=self.trainer.user)
        endpoint = self.base_url + \
            f'{self.team.pk}/pokemons/' + f'{self.pokemon.pk}'
        data = {
            'name': 'bulbasaur',
        }
        response = self.client.put(endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'bulbasaur')

    def test_pokemon_unauthorized(self):
        """
        Ensure we can't access pokemons without authentication.
        """
        self.client.force_authenticate(user=None)
        endpoint = self.base_url + f'{self.team.pk}/pokemons/'
        response = self.client.get(endpoint, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
