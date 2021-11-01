"""Users app."""

# Django
from django.apps import AppConfig


class UserAppConfig(AppConfig):
    """Users app config."""
    default_auto_field = 'django.db.models.AutoField'
    name = 'app.user'
    verbose_name = 'Users'
