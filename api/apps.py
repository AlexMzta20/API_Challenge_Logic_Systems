# Importa la clase AppConfig desde el módulo django.apps.
from django.apps import AppConfig


# Define una subclase de AppConfig llamada ApiConfig.
class ApiConfig(AppConfig):
    # Establece el tipo de campo que Django debe usar para las claves primarias automáticas.
    default_auto_field = 'django.db.models.BigAutoField'
    # Especifica el nombre de la aplicación. Django utilizará este nombre internamente.
    name = 'api'
