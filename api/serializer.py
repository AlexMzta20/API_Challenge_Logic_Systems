# Importa el módulo serializers de Django REST Framework.
from rest_framework import serializers
# Importa la clase Programmer desde el módulo models en el mismo directorio.
from .models import Programmer


# Define una clase ProgrammerSerializer que hereda de serializers.ModelSerializer.
class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:  # Define una subclase Meta dentro de ProgrammerSerializer.
        # Especifica que el modelo para este serializador que es Programmer.
        model = Programmer
        # fields = ('fullname','nickname')
        # Especifica que todos los campos del modelo deben ser incluidos en el serializador.
        fields = '__all__'
