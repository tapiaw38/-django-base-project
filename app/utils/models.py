"""Django base model utilities."""

# Django
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    """Base model."""

    created = models.DateTimeField('create at', auto_now_add=True)
    modified = models.DateTimeField('modified at', auto_now=True)

    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
