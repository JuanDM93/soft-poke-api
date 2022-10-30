from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    """
    Base model for all models
    """
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
