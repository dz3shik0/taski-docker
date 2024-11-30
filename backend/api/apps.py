"""Django application configuration for the API module.

This class configures the API app and sets the default
auto field type for models within this application.
"""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Модель приложения Api."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
