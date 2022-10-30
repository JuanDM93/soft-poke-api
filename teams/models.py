from django.db.models import (
    CharField,
    ForeignKey,
    ManyToManyField,
    CASCADE,
)

from pokeapi.utils.models import BaseModel
from trainers.models import Trainer
from pokemons.models import Pokemon


class Team(BaseModel):
    name = CharField(max_length=100)
    trainer = ForeignKey(
        Trainer,
        related_name='teams',
        on_delete=CASCADE
    )
    members = ManyToManyField(
        Pokemon,
        related_name='teams',
        blank=True,
        max_length=6,
    )

    def __str__(self):
        return self.name
