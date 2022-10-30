from django.db import models
from django.contrib.auth.models import User

from pokeapi.utils.models import BaseModel


class Trainer(BaseModel):
    """
    Owner of pokemon teams
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='trainer',
    )

    def __str__(self):
        return self.user.username
