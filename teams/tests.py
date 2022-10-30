from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from trainers.models import Trainer
from teams.models import Team


class TeamTests(APITestCase):
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

    def test_team_list(self):
        """
        Ensure we can list teams.
        """
        url = reverse('teams:team-list')
        self.client.force_authenticate(user=self.trainer.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.count(), 1)

    def test_team_detail(self):
        """
        Ensure we can retrieve a team.
        """
        url = reverse('teams:team-detail', kwargs={'pk': self.team.pk})
        self.client.force_authenticate(user=self.trainer.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team 1')

    def test_team_create(self):
        """
        Ensure we can create a team.
        """
        url = reverse('teams:team-list')
        data = {
            'name': 'Team 2',
            'trainer': self.trainer.pk,
        }
        self.client.force_authenticate(user=self.trainer.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(response.data['name'], 'Team 2')

    def test_team_update(self):
        """
        Ensure we can update a team.
        """
        url = reverse('teams:team-detail', kwargs={'pk': self.team.pk})
        data = {
            'name': 'Team 2',
            'trainer': self.trainer.pk,
        }
        self.client.force_authenticate(user=self.trainer.user)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team 2')

    def test_team_delete(self):
        """
        Ensure we can delete a team.
        """
        url = reverse('teams:team-detail', kwargs={'pk': self.team.pk})
        self.client.force_authenticate(user=self.trainer.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 0)
