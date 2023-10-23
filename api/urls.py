# Importa las funciones path e include del módulo django.urls.
from django.urls import path, include
# Importa el módulo routers de Django REST Framework.
from rest_framework import routers
from api import views  # Importa el módulo views desde la aplicación api.

# Crea una instancia de DefaultRouter y la asigna a la variable router.
# DefaultRouter es una clase que proporciona una forma sencilla de definir rutas para las vistas.
router = routers.DefaultRouter()
# Registra la vista ProgrammerViewSet con la ruta 'programmer' en el router.
router.register(r'programmer', views.ProgrammerViewSet)
# Define una lista de patrones de URL para tu aplicación.
urlpatterns = [
    # Incluye las rutas definidas en el router en la URL raíz ('').
    path('', include(router.urls))
]
