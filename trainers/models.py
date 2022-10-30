from django.db.models import (
    OneToOneField,
    CASCADE,
)
from django.contrib.auth.models import User

from pokeapi.utils.models import BaseModel


class Trainer(BaseModel):
    """
    Owner of pokemon teams
    """
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name='trainer',
    )

    def __str__(self):
        return self.user.username
