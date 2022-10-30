from django.db import models

from pokeapi.utils.models import BaseModel
from trainers.models import Trainer


class Team(BaseModel):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        Trainer,
        related_name='teams',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
