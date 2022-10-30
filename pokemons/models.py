from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
)

from pokeapi.utils.models import BaseModel
from trainers.models import Trainer


class Pokemon(BaseModel):
    """
    Pokemon model

    A pokemon must be owned by a trainer
    """

    name = CharField(max_length=100)
    trainer = ForeignKey(
        Trainer,
        related_name='pokemons',
        on_delete=CASCADE
    )

    def __str__(self):
        return self.name
