# Importa el módulo de administración de Django.
from django.contrib import admin
# Importa la clase Programmer desde el módulo models en el mismo directorio.
from .models import Programmer

# Register your models here. Aquí es dónde se deben registrar los modelos para el sitio de administración.
# Registra la clase Programmer en el sitio de administración de Django.
admin.site.register(Programmer)
