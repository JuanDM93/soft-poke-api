from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from trainers.models import Trainer


class TrainerTests(APITestCase):
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

    def test_trainer_list(self):
        """
        Ensure we can list trainers.
        """
        url = reverse('trainer-list')
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Trainer.objects.count(), 1)

    def test_trainer_detail(self):
        """
        Ensure we can retrieve a trainer.
        """
        url = reverse('trainer-detail', kwargs={'uuid': self.trainer.pk})
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'trainer')

    def test_trainer_signup(self):
        """
        Ensure we can signup a trainer.
        """
        url = reverse('trainer-signup')
        data = {
            'username': 'new_trainer',
            'password': 'new_trainer',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trainer.objects.count(), 2)
        self.assertEqual(response.data['username'], 'new_trainer')
