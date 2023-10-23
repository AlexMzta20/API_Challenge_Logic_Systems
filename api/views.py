# Importa el módulo viewsets de Django REST Framework.
from rest_framework import viewsets
# Importa la clase ProgrammerSerializer desde el módulo serializer en el mismo directorio.
from .serializer import ProgrammerSerializer
# Importa la clase Programmer desde el módulo models en el mismo directorio.
from .models import Programmer

# Create your views here. Aquí es dónde debemos crear las vistas

# Define una clase ProgrammerViewSet que hereda de viewsets.ModelViewSet.


class ProgrammerViewSet(viewsets.ModelViewSet):
    # Define un atributo queryset que es un QuerySet que contiene todas las instancias de Programmer.
    queryset = Programmer.objects.all()
    # Define un atributo serializer_class que es la clase ProgrammerSerializer.
    serializer_class = ProgrammerSerializer
